import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import DetailView, CreateView, UpdateView
from django.db.models import Sum
from .models import Post, Comment, PostVote


class CreatePostView(CreateView):
    model = Post
    template_name = "posts/create_post.html"
    success_url = reverse_lazy("home")
    fields = ['title', 'content', 'description', 'category', 'thumbnail']

    def form_valid(self, form):
        print('---------------------call form valid')
        form.instance.author = self.request.user.profile
        post = form.save(commit=False)
        return super().form_valid(form)


class PostView(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "posts/post.html"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views = obj.views + 1
        obj.save(update_fields=['views'])
        return obj


@require_POST
def comment(request, post_id):
    try:
        data = json.loads(request.body)
        content = data.get('content')
        post_id = data.get('post_id')
        profile = request.user.profile
    except (ValueError, TypeError, json.JSONDecodeError):
        return JsonResponse({"success": False, "error": "Invalid JSON input"}, status=400)

    if not content:
        return JsonResponse({"success": False, "error": "Empty Comment"})

    post = get_object_or_404(Post, id=post_id)
    comment = Comment.objects.create(
        post=post, commenter=profile, content=content)
    comment.save()
    return JsonResponse({
        "success": True,
        "username": profile.user.username,
        "content": comment.content,
        "created_at": comment.created_at.strftime("%B %d, %Y, %I:%M %p").lstrip('0').lower(),
        "avatar": profile.avatar.url
    })


@require_POST
def post_vote(request, post_id):
    try:
        data = json.loads(request.body)
        vote_choice = int(data.get('vote', 0))
    except (ValueError, TypeError, json.JSONDecodeError):
        return JsonResponse({"success": False, "error": "Invalid JSON input."}, status=400)

    profile = request.user.profile
    post = get_object_or_404(Post, pk=post_id)

    if vote_choice not in [PostVote.UPVOTE, PostVote.DOWNVOTE]:
        return JsonResponse({"success": False, "error": "Invalid vote value."}, status=400)

    vote, created = PostVote.objects.get_or_create(
        post=post,
        voted_by=profile,
        defaults={'value': vote_choice}
    )

    if created:
        message = "Vote added"
    else:
        if vote.value == vote_choice:
            vote.delete()
            message = "Vote removed"
            vote_choice = 0
        else:
            vote.value = vote_choice
            vote.save()
            message = "Vote updated"
    total_value = post.post_votes.aggregate(total=Sum('value'))['total'] or 0

    return JsonResponse({
        "success": True,
        "message": message,
        "votes": total_value,
        "vote_choice": vote_choice
    })


class UpdatePostView(UpdateView):
    model = Post
    template_name = "posts/update_post.html"
    success_url = reverse_lazy("home")
    fields = ['title', 'category', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        post = form.save(commit=False)

        return super().form_valid(form)


def post_create(request):
    return render(request, template_name="posts/create.html")

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect

from apps.users.models import Profile

from . models import Conversation, Message


def index(request):
    return render(request, "chat/messenger.html")


def to(request, profile_id):
    if int(profile_id) == request.user.profile.id:
        return redirect("home")

    profile = Profile.objects.get(pk=int(profile_id))
    conversation = Conversation.objects.filter(
        members=request.user.profile).filter(members=profile).first()
    if not conversation:
        conversation = Conversation.create_with_members(
            request.user.profile, profile)

    return redirect("chat:conversation", conversation_id=conversation.id)


def conversation_view(request, conversation_id):
    conversation = Conversation.objects.get(pk=conversation_id)
    return render(request, "chat/messenger.html", {"conversation": conversation})


def send_message(request):
    if request.method == "POST":
        conv_id = request.POST.get('conversation_id')
        sender_id = request.POST.get('sender_id')
        receiver_id = request.POST.get('receiver_id')
        content = request.POST.get('content')
        
        conversation = get_object_or_404(Conversation, id=int(conv_id))
        sender = get_object_or_404(Profile, id=int(sender_id))
        receiver = get_object_or_404(Profile, id=int(receiver_id))
        message = Message.objects.create(conversation=conversation, sender=sender, receiver=receiver, content=content)
        return JsonResponse({
            "success": True,
            "sender": sender,
            "receiver": receiver,
            "content": content
        })
    else:
        return JsonResponse({"success": False, "error": "Invalid request"})

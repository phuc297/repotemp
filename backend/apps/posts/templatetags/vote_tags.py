from django import template

register = template.Library()


@register.filter
def user_upvote(post, profile_id):
    return post.get_user_vote(profile_id) == 1


@register.filter
def user_downvote(post, profile_id):
    return post.get_user_vote(profile_id) == -1

from django import template

register = template.Library()


@register.filter
def is_following(user_profile, profile):
    if user_profile.following.filter(pk=profile.pk).exists():
        return True
    return False


@register.filter
def is_not_following(user_profile, profile):
    if not user_profile.following.filter(pk=profile.pk).exists():
        return True
    return False

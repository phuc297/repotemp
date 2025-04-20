from django import template

from apps.chat.models import Conversation

register = template.Library()

def get_other_member(conversation: Conversation, current_member):
    return conversation.get_other_member(current_member)

register.filter("get_other_member", get_other_member)
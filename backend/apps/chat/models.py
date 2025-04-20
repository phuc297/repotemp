from django.db import models
from django.forms import ValidationError

from apps.users.models import Profile


class Conversation(models.Model):
    title = models.TextField(blank=True)
    members = models.ManyToManyField(Profile, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @classmethod
    def create_with_members(cls, member1, member2):
        conv = cls()
        conv.save()
        conv.members.add(member1, member2)
        conv.title = f"{member1} and {member2}"
        conv.save()
        return conv

    def get_other_member(self, current_member):
        return self.members.exclude(id=current_member.id).first()


class Message(models.Model):
    conversation = models.ForeignKey(
        Conversation, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(
        Profile, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(
        Profile, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def clean(self):
        if self.sender not in self.conversation.members.all():
            raise ValidationError(
                "Sender must be a member of the conversation.")
        if self.receiver not in self.conversation.members.all():
            raise ValidationError(
                "Receiver must be a member of the conversation.")
        if self.sender == self.receiver:
            raise ValidationError("Sender and receiver cannot be the same.")
        return super().clean()

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.sender} to {self.receiver}: {self.content}"

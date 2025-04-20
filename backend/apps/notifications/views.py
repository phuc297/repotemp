from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Notification


def index(request):
    return render(request, "notifications/notifications.html")


class NotificationView(TemplateView):
    context_object_name = "notifications"
    template_name = "notifications/notification.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notifications'] = Notification.objects.filter(recipient_id=int(self.request.user.profile.id)).order_by('-timestamp')
        return context
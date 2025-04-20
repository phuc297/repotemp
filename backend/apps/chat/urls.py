from django.urls import path

from . import views

app_name = 'chat'
urlpatterns = [
    path("", views.index, name="index"),
    path("to/<int:profile_id>/", views.to, name="to"),
    path("<int:conversation_id>/", views.conversation_view, name="conversation"),
]

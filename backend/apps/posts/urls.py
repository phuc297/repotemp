from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('<int:pk>', views.PostView.as_view(), name='view'),
    path("<int:post_id>/comment/", views.comment, name="comment"),
    path("<int:post_id>/vote/", views.post_vote, name="vote"),
    path("create/", views.CreatePostView.as_view(), name="create"),
    path("update/<int:pk>", views.UpdatePostView.as_view(), name="update"),
]

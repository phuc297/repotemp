from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('<int:pk>', views.ProfileView.as_view(), name='profile'),
    path('<int:profile_id>/follow', views.follow_profile, name='follow'),
    path('<int:profile_id>/follow_button/', views.follow_button, name='follow_button'),
]

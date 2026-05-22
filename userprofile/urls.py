from django.urls import path
from userprofile import views

urlpatterns = [
    path('profile/', views.user_profile, name="profile"),
    path('user/<str:username>/', views.public_profile, name="public_profile"),
]

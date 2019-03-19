from django.urls import path
from userprofile import views

urlpatterns = [
    path('profile/', views.user_profile, name="profile")
]

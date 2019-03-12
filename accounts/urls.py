from django.urls import path, include
from accounts.views import logout, login, registration, auth_index, user_profile

urlpatterns = [
    path('logout/', logout, name="logout"),
    path('login/', login, name="login"),
    path('register/', registration, name="registration"),
    path('auth_index/', auth_index, name="auth_index"),
    path('profile/', user_profile, name="profile"),
    path('reset/', include('accounts.url_reset')),
]
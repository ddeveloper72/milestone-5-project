from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('health/', views.health_check, name='health_check'),
    path('keep-alive/', views.keep_alive, name='keep_alive'),
]
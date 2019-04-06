from django.urls import path, re_path
from cart import views

urlpatterns = [
    path('', view.view_cart, name='view_cart'),
    re_path(r'^add/(?P<id>\d+)', vieww.add_to_cart, name='add_to_cart'),
    re_path(r'^adjust/(?P<id>\d+)', view.adjust_cart, name='adjust_cart'),
    ]

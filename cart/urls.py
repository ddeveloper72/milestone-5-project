from django.urls import path, re_path
from cart import views

urlpatterns = [
    path('', views.view_cart,
         name='view_cart'),
    re_path(r'^add/(?P<pk>\d+)', views.add_to_cart,
            name='add_to_cart'),
    re_path(r'^adjust/(?P<pk>\d+)', views.adjust_cart,
            name='adjust_cart'),
    ]

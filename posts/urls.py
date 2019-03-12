from django.urls import path, include
from posts.views import get_posts, post_detail, create_or_edit_a_post

# CRUD operation url templates
urlpatterns = [
    path('', get_posts, name='get_posts'), 
    path('(?P<pk>\d+)$', post_detail, name='post_detail'), 
    path('new/$', create_or_edit_a_post, name='new_post'),
    path('(?P<pk>\d+)/edit/$', create_or_edit_a_post, name='edit_post'path),
]
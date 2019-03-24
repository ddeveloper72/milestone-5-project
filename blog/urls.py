from django.urls import path, re_path
from blog import views

# CRUD operation url templates
urlpatterns = [
    path('', views.get_posts,
         name='get_posts'),
    re_path(r'^(?P<pk>\d+)$', views.post_detail,
            name='post_detail'),
    re_path(r'^new/$', views.create_or_edit_a_post,
            name='new_post'),
    re_path(r'^(?P<pk>\d+)/edit/$', views.create_or_edit_a_post,
            name='edit_post'),
    path('add_comment/<int:pk>/new_comment/', views.add_comment_to_post,
         name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve,
         name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove,
         name='comment_remove'),
]
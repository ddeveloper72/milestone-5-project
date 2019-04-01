from django.urls import path, re_path
from issue_tracker import views


# CRUD operation url templates
urlpatterns = [
    path('', views.get_issues,
         name='get_issues'),
    re_path(r'^(?P<pk>\d+)/$', views.issue_detail,
            name='issue_detail'),
    re_path(r'^new/$', views.new_issue,
            name='new_issue'),
    re_path(r'^(?P<pk>\d+)/edit/$', views.edit_issue,
            name='edit_issue'),
    re_path(r'^(?P<pk>\d+)/vote/(?P<category>.+)/$', views.upvote,
            name='upvote'),
    path('add_comment/<int:pk>/new_comment', views.add_comment_to_issue,
         name='add_comment_to_issue'),
    path('comment/<int:pk>/approve/', views.comment_for_issue_approve,
         name='comment_for_issue_approve'),
    path('comment/<int:pk>/remove/', views.comment_for_issue_remove,
         name='comment_for_issue_remove'),
]

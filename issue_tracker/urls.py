from django.urls import path, re_path
from issue_tracker import views


# CRUD operation url templates
urlpatterns = [
    path('', views.get_issues,
         name='get_issues'),
    re_path(r'^(?P<pk>\d+)$', views.issue_detail,
            name='issue_detail'),
    re_path(r'^new/$', views.create_or_edit_a_issue,
            name='new_issue'),
    re_path(r'^(?P<pk>\d+)/edit/$', views.create_or_edit_a_issue,
            name='edit_issue'),
    path('add_comment/<int:pk>/new_comment', views.add_comment_to_issue,
         name='add_comment_to_issue'),
    path('comment/<int:pk>/approve/', views.comment_for_issue_approve,
         name='comment_for_issue_approve'),
    path('comment/<int:pk>/remove/', views.comment_for_issue_remove,
         name='comment_for_issue_remove'),
]

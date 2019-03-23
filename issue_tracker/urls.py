from django.urls import path, re_path
from issue_tracker import views


# CRUD operation url templates
urlpatterns = [
    path('', views.get_issues,
         name='get_issues')
]
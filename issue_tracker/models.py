from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class IssuesList(models.Model):
    """
    The issues list needs allows a user to raise an issue for the
    development team to review.
    """
    title = models.CharField(max_length=140)
    task_list = models.ForeignKey(TaskList,
                                  on_delete=models.CASCADE,
                                  null=True)
    created_date = models.DateTimeField(blank=True, null=True,
                                        default=timezone.now)
    completed = models.BooleanField(default=False)
    completed_date = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey(
        settings.User,
        null=True,
        on_delete=models.CASCADE,
    )
    content = models.TextField(blank=True, null=True)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=60, blank=True, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    priority = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Like the blog, a user can comment on an issue posted by another user.
    """
    author = models.ForeignKey(
        settings.User, on_delete=models.CASCADE, blank=True, null=True
    )
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.datetime.now)
    comment = models.TextField(blank=False)
    issue = models.ForeignKey(Bug, default=None, on_delete=models.CASCADE)
    is_reported = models.BooleanField(default=False)
    is_hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.comment

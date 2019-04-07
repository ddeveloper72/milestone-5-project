from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

# Bug Categories

ISSUE_GENRE = (
    ('Navigation', 'Navigation'),
    ('Flight Controls', 'Flight Controls'),
    ('Auto Pilot', 'Auto Pilot'),
    ('None', 'None'),
)

CATEGORY_GENRE = (
    ('BUG', 'BUG'),
    ('FEATURE ', 'FEATURE'),
)

TICKET_STATUS = (
    ('To do', 'To do'),
    ('In Progress', 'In Progress'),
    ('Complete', 'Complete'),
)


class Issue(models.Model):
    """
    The issues list needs allows a user to raise an issue for the
    development team to review.
    """
    title = models.CharField(max_length=140)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True,
                                          default=timezone.now)
    completed = models.BooleanField(default=False)
    completed_date = models.DateTimeField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=60, blank=True, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    author = models.ForeignKey(User, default=None,
                               related_name="issue_author",
                               on_delete=models.CASCADE)
    genre = models.CharField(max_length=30, choices=ISSUE_GENRE,
                             default='None')
    category = models.CharField(max_length=10, choices=CATEGORY_GENRE,
                                default='BUG')
    status = models.CharField(max_length=10, choices=TICKET_STATUS,
                              default='To do')
    votes = models.IntegerField(default=0)
    voter = models.ManyToManyField(User, related_name='issue_upvoters',
                                   default=None,)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, default=80.00)

    class Meta:
        ordering = ['-created_date']

    def __unicode__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


class Comment(models.Model):
    """
    Like the blog, a user can comment on an issue posted by another user.
    """
    comment = models.TextField(blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, default=None, 
                               related_name="issue_comment_author",
                               on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, default=None, on_delete=models.CASCADE,
                              related_name='comments')
    approved_comment = models.BooleanField(default=False)
    is_reported = models.BooleanField(default=False)
    is_hidden = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.comment


class UserSeenIssue(models.Model):
    user = models.ForeignKey(User, default=None, related_name='seen_issue',
                             on_delete=models.CASCADE)
    post = models.ForeignKey(Issue, on_delete=models.CASCADE)


class UserVoted(models.Model):
    user = models.ForeignKey(User, default=None, related_name='has_voted',
                             on_delete=models.CASCADE)
    post = models.ForeignKey(Issue, on_delete=models.CASCADE)

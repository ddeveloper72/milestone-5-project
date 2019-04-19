from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.html import mark_safe
from markdown import markdown

# Create your models here.


class Post(models.Model):
    """
    A single blog post
    """
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True,
                                          default=timezone.now)
    content = models.TextField(blank=True, null=True)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=60, blank=True, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    author = models.ForeignKey(User, default=None,
                               related_name="blog_author",
                               on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        ordering = ['-created_date']

    def get_content_as_markdown(self):
        return mark_safe(markdown(self.content, safe_mode='escape'))

    def __unicode__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


class Comment(models.Model):
    """
    A comment following a blog post
    """
    comment = models.TextField(blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User, default=None, related_name="blog_comment_author",
        on_delete=models.CASCADE)
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE,
                             related_name='comments')
    approved_comment = models.BooleanField(default=False)
    is_reported = models.BooleanField(default=False)
    is_hidden = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.comment


class UserSeenPosts(models.Model):
    user = models.ForeignKey(User, default=None, related_name='seen_posts',
                             on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

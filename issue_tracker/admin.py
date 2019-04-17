from django.contrib import admin
from .models import Issue, Comment, UserSeenIssue, UserVoted, UserVotedFeature

# Register your models here.

admin.site.register(Issue)
admin.site.register(Comment)
admin.site.register(UserSeenIssue)
admin.site.register(UserVoted)
admin.site.register(UserVotedFeature)

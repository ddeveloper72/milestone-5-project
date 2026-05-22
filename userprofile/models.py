from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=50, blank=True, 
                                   help_text="Public name shown on your posts (defaults to username if not set)")
    bio = models.TextField(max_length=500, blank=True,
                          help_text="Tell others about yourself (visible on your public profile)")
    location = models.CharField(max_length=30, blank=True,
                               help_text="Optional - only shown if you enable 'Show location on profile'")
    birth_date = models.DateField(null=True, blank=True,
                                 help_text="Private - never shown publicly")
    
    # Privacy settings - GDPR compliance
    show_location = models.BooleanField(default=False,
                                       help_text="Make your location visible on your public profile")
    
    def get_display_name(self):
        """Return display name or username if not set"""
        return self.display_name if self.display_name else self.user.username
    
    def __str__(self):
        return f"{self.user.username}'s profile"

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
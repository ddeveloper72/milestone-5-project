from django.contrib import admin
from .models import UserProfile
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    search_fields = ('bio',)
    list_display = ('user', 'location', 'bio', )


admin.site.register(UserProfile, UserProfileAdmin)

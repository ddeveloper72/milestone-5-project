from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['display_name', 'bio', 'location', 'birth_date', 'show_location']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }

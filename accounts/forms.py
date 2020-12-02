from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class UserloginForm(forms.Form):
    """
    Form for user to input login details
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


# enforce users provide a unique email
class uniqueEmailForm:
    def clean_email(self):
        qs = User.objects.filter(email=self.cleaned_data['email'])
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.count():
            raise forms.ValidationError(
                'That email address is already in use')
        else:
            return self.cleaned_data['email']


class UserRegistrationForm(UserCreationForm, uniqueEmailForm):
    """
    Form is used to register the user
    """
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password Confirmation",
        widget=forms.PasswordInput)

    class Meta:
        """
        Inner class is used by Django to provide infomation about the forms.
        """
        model = User
        """
        Specifies the name of the model where we want to store user information
        """
        fields = ['username', 'email', 'password1', 'password2']


    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise forms.ValidationError("Please confirm your password")

        if password1 != password2:
            raise forms.ValidationError("Passwords must match")
        return password2


class UserNameForm(forms.ModelForm, uniqueEmailForm):
    """
    Form is used to register first and last name
    """

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'special'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'special'}))
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


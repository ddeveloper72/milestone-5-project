from django import forms
from .models import Issue, Comment


class AddEditIssueFrom(forms.ModelForm):

    class Meta:
        model = Issue
        fields = ('title', 'content', 'image', 'tag', 'published_date',
                  'genre', 'category')

        widgets = {
            'title': forms.TextInput(
                    attrs={'placeholder': 'Add an issue'}),
            'content': forms.Textarea(
                    attrs={'placeholder': 'Add the details about your issue'}),
            'tag': forms.TextInput(
                    attrs={'placeholder': 'keywords identifying issue'})
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('comment',)

        widgets = {
            'comment': forms.widgets.TextInput(
                    attrs={'placeholder': 'Add a comment about this issue?'})
        }


class IssueStatusForm(forms.ModelForm):

    class Meta:
        model = Issue
        fields = ['status', ]

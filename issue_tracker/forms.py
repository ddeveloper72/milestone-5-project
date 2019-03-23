from django import forms
from .models import IssuesList, Comment


class AddEditIssueFrom(forms.ModelForm):

    class Meta:
        model = IssuesList
        fields = ['title', 'content', 'created_date', 'created_by']

    widgets = {
        'title' = forms.CharField(
            widget=forms.widgets.TextInput(
                attrs={'placeholder': 'Add an issue'})),
        'content' = forms.CharField(
            widget=forms.Textarea(),
            required=False),
        'tag': forms.TextInput(attrs={'placeholder':
                                      'keywords identifying issue'})
    }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('comment',)

    widgets = {
        'comment' = forms.CharField(
            widget=forms.widgets.TextInput(
                attrs={'placeholder': 'Add a comment about this issue?'}))
    }

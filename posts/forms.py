from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'tag', 'published_date')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder':
                                            'Post Title'}),
            'content': forms.Textarea(attrs={'placeholder':
                                             'About your post here...'}),
            'tag': forms.TextInput(attrs={'placeholder':
                                          'keywords identifying items'})
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('comment',)

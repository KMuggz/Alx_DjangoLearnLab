from django import forms
from .models import Post, Comment
from taggit.forms import TagWidget
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Add a comment...'
                }),
        }

class PostForm(forms.ModelForm):
    tags = forms.CharField(widget=TagWidget(), required=False) # Highlight: Explicitly declaring the tags field
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags'] # Highlight: Added tags
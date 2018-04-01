from django.contrib.auth.models import User
from django import forms

from .models import Posts
from .models import Comments


class UserForm(forms.ModelForm):
    # Changes it from plain text to hashing
    password = forms.CharField(widget=forms.PasswordInput)

    # Meta Information about your class.
    class Meta:
        model = User
        # What fields do we want to appear on the form?
        fields = ['username', 'email', 'password']


class LoginForm(forms.ModelForm):
    # Changes it from plain text to hashing
    password = forms.CharField(widget=forms.PasswordInput)

    # Meta Information about your class.
    class Meta:
        model = User
        # What fields do we want to appear on the form?
        fields = ['username', 'password']


class PostForm(forms.ModelForm):
    image = forms.FileField(label="Select an image to upload.", help_text="Maximum file size is 2 megabytes")

    class Meta:
        model = Posts
        fields = ['title', 'location', 'hazard_type', 'description']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment_body']
from django.contrib.auth.models import User
from django import forms
from .models import Posts
from .models import Comments
from .models import PostImageCollection

from .validators import validate_image_file
from .validators import validate_address


class UserForm(forms.ModelForm):
    # Changes it from plain text to hashing
    password = forms.CharField(widget=forms.PasswordInput)

    # Meta Information about your class.
    class Meta:
        model = User
        # What fields do we want to appear on the form?
        fields = ['username', 'email', 'password']


class LoginForm(forms.ModelForm):
    # Changes it from pslain text to hashing
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        # What fields do we want to appear on the form?
        fields = ['username', 'password']


class SearchForm(forms.Form):
    select_choices = (
        ('description', 'Description'),
        ('username', 'Username'),
        ('location', 'Location'),
        ('title', "Title"),
        ('hazard_type', "Hazard Type")
    )
    selection = forms.ChoiceField(widget=forms.Select, choices=select_choices)
    value = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Ex: Lake'}))


class PostForm(forms.ModelForm):
    location = forms.CharField(validators=[validate_address])

    class Meta:
        model = Posts
        fields = ['title', 'location', 'hazard_type', 'description']


class ImageForm(forms.ModelForm):
    image1 = forms.ImageField(validators=[validate_image_file])
    image2 = forms.ImageField(validators=[validate_image_file])
    image3 = forms.ImageField(validators=[validate_image_file])
    image4 = forms.ImageField(validators=[validate_image_file])

    class Meta:
        model = PostImageCollection
        fields = ['image1', 'image2', 'image3', 'image4']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment_body']

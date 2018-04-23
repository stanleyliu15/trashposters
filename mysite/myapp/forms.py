from django.contrib.auth.models import User
from django import forms
from .models import Posts
from .models import Comments
from .models import PostImageCollection

from .validators import validate_image_file
from .validators import validate_address


class UserForm(forms.ModelForm):
    """
    Form to register new users to the website.
    Passwords are turned into starts with the PasswordInput widget.
    Username, email, and password are required.
    This form is based off of the django.contrib.auth.models.User model.
    """
    password = forms.CharField(widget=forms.PasswordInput)

    # Meta Information about your class.
    class Meta:
        model = User
        # What fields do we want to appear on the form?
        fields = ['username', 'email', 'password']


class LoginForm(forms.ModelForm):
    """
    Form to log in users to the website.
    Passwords are turned into starts with the PasswordInput widget.
    Username and password are required.
    This form is based off of the django.contrib.auth.models.User model.
    """
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        # What fields do we want to appear on the form?
        fields = ['username', 'password']


class SearchForm(forms.Form):
    """
    Form to search the website.
    User selects a search algorithm with the drop down menu and enters a query.
    Query is stored as the value in this form.
    """
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
    """
    Form to post to the website.
    Validates location by checking if it generates a valid latitude.
    Title, location, hazard_type, and description are required.
    This form is based off of the myapp.models.Posts model.
    """
    location = forms.CharField(validators=[validate_address])

    class Meta:
        model = Posts
        fields = ['title', 'location', 'hazard_type', 'description']


class ImageForm(forms.ModelForm):
    """
    Form to post multiple images to the same post.
    Validates whether or not a file is an image before posting.
    This form is based off of the myapp.models.PostImageCollection model.
    """
    image1 = forms.ImageField(validators=[validate_image_file])
    image2 = forms.ImageField(validators=[validate_image_file])
    image3 = forms.ImageField(validators=[validate_image_file])
    image4 = forms.ImageField(validators=[validate_image_file])

    class Meta:
        model = PostImageCollection
        fields = ['image1', 'image2', 'image3', 'image4']


class CommentForm(forms.ModelForm):
    """
    Form to post comments onto a post.
    TODO: Implement this form in code and make appropriate changes to this class.
    """
    class Meta:
        model = Comments
        fields = ['comment_body']

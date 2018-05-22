from django.contrib.auth.models import User
from django import forms
from .models import *

from .validators import *



hazard_types_choices = {
    ('smoke', 'Smoke'),
    ('water', 'Water'),
    ('air', 'Air'),
    ('poison', 'Poison'),
    ('lead', 'Lead'),
    ('fire', 'Fire'),
    ('biohazard', 'Biohazard'),
    ('oil spill', 'Oil Spill'),
    ('nuclear waste', 'Nuclear Waste'),
    ('trash', 'Trash'),
}


class UserSignUpForm(forms.ModelForm):
    """
    Form to sign up users with. Input attributes moved from
    HTML to here in order to keep using django's validation system.
    """
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'text',
               'class': 'form-control',
               'id': 'firstname',
               'name': 'firstname'
               }),
        label="First Name")
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'text',
               'class': 'form-control',
               'id': 'lastname',
               'name': 'lastname'
               }),
        label="Last Name")
    username = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'text',
               'class': 'form-control',
               'id': 'username',
               'name': 'username'
               }),
        label="Username")
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'type': 'text',
               'class': 'form-control',
               'id': 'email',
               'name': 'email'
               }),
        label="Email")
    re_email = forms.EmailField(widget=forms.TextInput(
        attrs={'type': 'text',
               'class': 'form-control',
               'id': 're_email',
               'name': 're_email'
               }),
        label="Confirm Email")
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control',
               'id': 'password',
               'name': 'password'
               }),
        label="Password")
    re_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control',
               'id': 're_password',
               'name': 're_password'
               }),
        label="Confirm Password")
    # Overrides the field order so that email and password verification are grouped together.
    field_order = ['first_name', 'last_name', 'username', 'email', 're_email', 'password', 're_password']

    def clean(self):
        """
        Extends the clean() function so that the form throws ValidationErrors
        if the passwords and emails don't match.
        :return: cleaned_data if everything looks good.
        :raisesL Validation errors if the fields don't match.
        """
        email = self.cleaned_data.get('email', None)
        re_email = self.cleaned_data.get('re_email', None)
        password = self.cleaned_data.get('password', None)
        re_password = self.cleaned_data.get('re_password', None)
        if email and re_email and (email == re_email):
            if password and re_password and (password == re_password):
                return self.cleaned_data
            raise forms.ValidationError("Your passwords don't match")
        else:
            raise forms.ValidationError("Your emails don't match")

    class Meta:
        """
        Metadata for the form to match it up with a model.
        """
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']


class UserDataForm(forms.ModelForm):
    """
    Form used to create user data during signup.
    Validates city and state.
    """
    city = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'text',
               'class': 'form-control',
               'id': 'city',
               'name': 'city'
               }),
        label="City",
        validators=[validate_city]
    )
    state = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'text',
               'class': 'form-control',
               'id': 'state',
               'name': 'state'
               }),
        label="State",
        validators=[validate_state])

    class Meta:
        model = UserData
        fields = ['city', 'state']


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


class LoginForm(forms.Form):
    """
    Form to log in users to the website.
    Passwords are turned into starts with the PasswordInput widget.
    Username and password are required.
    This form is based off of the django.contrib.auth.models.User model.
    """
    username = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'text',
               'class': 'form-control',
               'id': 'username',
               'name': 'username',
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'type': 'password',
               'class': 'form-control',
               'id': 'password',
               'name': 'password',
        }
    ))

    class Meta:
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
    title = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'text',
               'class': 'form-control',
               'id': 'title',
               'name': 'title'
               'placeholder:' 'Enter a title'
               }),
        label="Title")
    hazard_type = forms.ChoiceField(choices=hazard_types_choices,
                                    widget=forms.Select(
                                     attrs=
                                     {
                                        'class': 'custom-select resize-select h-100 py-0 d-none d-sm-block',
                                        'id': 'hazardtype',
                                        'name': "hazardtype",
                                        'autocomplete': 'off'
                                     }))
    location = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'text',
               'class': 'form-control',
               'id': 'location',
               'name': 'location'
               'placeholder:' 'Enter an address'
               }),
        label="Location",
        validators=[validate_address])
    description = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'text',
               'class': 'form-control',
               'id': 'description',
               'name': 'description'
               'placeholder:' 'Enter a description'
               }),
        label="Description")

    # Overrides the field order so that email and password verification are grouped together.
    field_order = ['title', 'hazard_type', 'location', 'description']

    class Meta:
        model = Posts
        fields = ['title', 'location', 'description']



class ImageForm(forms.ModelForm):
    """
    Form to post multiple images to the same post.
    Validates whether or not a file is an image before posting.
    This form is based off of the myapp.models.PostImageCollection model.
    """
    image1 = forms.ImageField(widget=forms.FileInput(
        attrs={
            'type': 'file',
            'class': 'custom-file-input',
            'id': 'post-image',
            'name': 'post_image',
            'aria-describedby': 'file-upload-help'
        }),
        validators=[validate_image_file],
        label='Upload Image',
        required=True)
    image2 = forms.ImageField(widget=forms.FileInput(
        attrs={
            'type': 'file',
            'class': 'custom-file-input',
            'id': 'post-image',
            'name': 'post_image',
            'aria-describedby': 'file-upload-help'
        }),
        validators=[validate_image_file],
        label='Upload Image',
        required=False)
    image3 = forms.ImageField(widget=forms.FileInput(
        attrs={
            'type': 'file',
            'class': 'custom-file-input',
            'id': 'post-image',
            'name': 'post_image',
            'aria-describedby': 'file-upload-help'
        }),
        validators=[validate_image_file],
        label='Upload Image',
        required=False)
    image4 = forms.ImageField(widget=forms.FileInput(
        attrs={
            'type': 'file',
            'class': 'custom-file-input',
            'id': 'post-image',
            'name': 'post_image',
            'aria-describedby': 'file-upload-help'
        }),
        validators=[validate_image_file],
        label='Upload Image',
        required=False)


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

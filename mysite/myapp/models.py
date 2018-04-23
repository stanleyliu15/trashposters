from django.db import models

from django.urls import reverse
from django.contrib.auth.models import User

"""
Note: Always perform migrations when making a change to models.py
in order to have the changes reflect in the database.

Models data type                            MySQL Equivalent
models.AutoField(primary_key=True)          integer AUTO_INCREMENT NOT NULL
models.CharField(maxLength=N)               varChar(N) NOT NULL
models.DateTimeField()                      datetime NOT NULL
models.ForeignKey(to, onDelete, options)    FOREIGN KEY
models.IntegerField()                       integer NOT NULL
"""

# TODO Extend the Users class from django.contrib.auth.models instead.
# Deleted the last one since it wasn't even being used in the current state of the website.


class HazardType(models.Model):
    """
    Locations:
        category_id - INT, Primary Key
        category - VARCHAR(255)
    """
    hazard_id = models.AutoField(primary_key=True)
    hazard_name = models.CharField(max_length=255)

    def __str__(self):
        return self.hazard_name


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.username.id, filename)


class UserData(models.Model):
    """
    User_data
        user_id - INT, Primary Key
        username = ForeignKey
        biography - VarChar
        location = VarChar
        avatar = VarChar
    """
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    biography = models.CharField(max_length=400, null=True)
    location = models.CharField(max_length=255, null=True)
    avatar = models.ImageField(upload_to=user_directory_path, null=True)

    def get_absolute_url(self):
        return reverse('profile_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.username) + "'s profile"


def post_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'post_{0}/{1}'.format(instance.post_id, filename)


class Posts(models.Model):
    """
    Posts:
        post_id - INT, Primary Key, Auto Increment
        user_id - INT, FOREIGN KEY
        location - VARCHAR(255), FOREIGN KEY
        hazard_type = VARCHAR(255), FOREIGN KEY

        title = VARCHAR(255)
        description - VARCHAR(400)
        date - DATE
    """
    post_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    hazard_type = models.ForeignKey(HazardType, on_delete=None)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=400)
    date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.post_id)


class PostImageCollection(models.Model):
    post_image_collection_id = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to=post_directory_path, null=True)
    image2 = models.ImageField(upload_to=post_directory_path, null=True)
    image3 = models.ImageField(upload_to=post_directory_path, null=True)
    image4 = models.ImageField(upload_to=post_directory_path, null=True)

    def __str__(self):
        return str(self.post_image_collection_id) + "for post: " + str(self.post_id)


class Comments(models.Model):
    """
    Comments:
        comment_id - INT, Primary Key, Auto Increment
        user_id - INT, FOREIGN KEY
        post_id = INT, FOREIGN KEY

        comment_body - VARCHAR(255)
    """
    comment_id = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    comment_body = models.CharField(max_length=255)


class Message(models.Model):
    """
    Messages:
        user_id1 - INT
        user_id2 - INT
        messages - TEXT
        Dates - DATETIME
    """
    user_id1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_userid1")
    user_id2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_userid2")
    messages = models.CharField(max_length=400)
    dates = models.DateTimeField()

    def __str__(self):
        return self.messages


class DummyTable(models.Model):
    name = models.CharField(default="Water makes the frogs turn gay.", max_length=255)
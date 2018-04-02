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


class UserData(models.Model):
    """
    User_data
        user_id - INT, Primary Key
        biography - TEXT
    """
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    biography = models.CharField(max_length=400)
    location = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='profile_pictures', null=True)

    def get_absolute_url(self):
        return reverse('profile_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.username) + "'s profile"


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
    image = models.ImageField(upload_to='posts/%Y/%m/%d', null=True)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.post_id)


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
from django.db import models

from django.urls import reverse
from django.contrib.auth.models import User

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

"""
Note: Always perform migrations when making a change to models.py
in order to have the changes reflect in the database.ata type                            MySQL Equivalent
models.AutoField(primary_key=True)          integer AUTO_INCREMENT NOT NULL
models.CharField(maxLength=N)               varChar(N) NOT NULL
models.DateTimeField()                      datetime NOT NULL
models.ForeignKey(to, onDelete, options)    FOREIGN KEY
models.IntegerField()                       integer NOT NULL
"""

# Possible status choices for a post.
STATUS_CHOICE = (
    ('In progress', 'In progress'),
    ('Being taken care of', 'Being taken care of'),
    ('Hazard eliminated', 'Hazard eliminated'))


class HazardType(models.Model):
    """
    Locations:
        category_id - INT, Primary Key
        category - VARCHAR(255)
    """
    hazard_id = models.AutoField(primary_key=True)
    hazard_name = models.CharField(max_length=255)

    def __str__(self):
        """
        Returns the string representation of this class.
        :return: a string representation of this class.
        """
        return self.hazard_name


def user_directory_path(instance, filename):
    """
    file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    :param instance:
    :param filename:
    :return: None
    """
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
    city = models.CharField(max_length=255, default="San Francisco")
    state = models.CharField(max_length=255, default="CA")
    avatar = models.ImageField(upload_to=user_directory_path, null=True)
    city_official = models.BooleanField(default=False)
    location = models.CharField(max_length=255, default="San Francisco")

    def get_first_name(self):
        user = User.objects.get(username=self.username)
        first_name = user.first_name
        return first_name

    def get_last_name(self):
        user = User.objects.get(username=self.username)
        last_name = user.last_name
        return last_name

    def get_absolute_url(self):
        return reverse('profile_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.username) + "'s profile"


def post_directory_path(instance, filename):
    """
    file will be uploaded to MEDIA_ROOT/post_<post_id>/<filename>
    :param instance:
    :param filename:
    :return:
    """
    return 'post_{0}/{1}'.format(instance.post_id, filename)


def post_preview_directory_path(instance, filename):
    """
    file will be uploaded to MEDIA_ROOT/post_<id>/preview/s<filename>
    :param instance:
    :param filename:
    :return:
    """
    return 'post_{0}/preview/{1}'.format(instance.post_id, filename)


class Posts(models.Model):
    """
    SQL Table for posts:
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
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    hazard_type = models.ForeignKey(HazardType, on_delete=None)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=400)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICE, default="In progress")
    preview_image = models.ImageField(upload_to=post_preview_directory_path, null=True)
    #full_image = models.ImageField(upload_to=post_directory_path, null=True)
    image_thumbnail = ImageSpecField(source='preview_image',
                                     processors=[ResizeToFill(50, 50)],
                                     format='JPEG',
                                     options={'quality': 60})
    image_regular = ImageSpecField(source='preview_image',
                                     processors=[ResizeToFill(200, 200)],
                                     format='JPEG',
                                     options={'quality': 80})
    city_official = models.BooleanField(default=False)

    def get_absolute_url(self):
        """
        Given a post id, returns a post_detail page with that id.
        :return:    A post detail page.
        """
        return reverse('post_detail', kwargs={'pk': self.pk})

    @staticmethod
    def search_by_username(username):
        """
        Given a query, returns a set of matching posts.
        :param username: The username of the poster in string form
        :return: A list of posts that meet the given criteria.
        """
        matching_posts = Posts.objects.filter(user_id__username__icontains=username)
        return matching_posts

    @staticmethod
    def search_by_location(location):
        """
        Given a query, returns a set of matching posts.
        :param location: The location of the post in string form.
        :return: A list of posts that meet the given criteria.
        """
        matching_posts = Posts.objects.filter(location__icontains=location)
        return matching_posts

    @staticmethod
    def search_by_title(title):
        """
        Given a query, returns a set of matching posts.
        :param title: The title of the post in string form
        :return: A list of posts that meet the given criteria.
        """
        matching_posts = Posts.objects.filter(title__icontains=title)
        return matching_posts

    @staticmethod
    def search_by_hazard_type(hazard_type):
        """
        Given a query, returns a set of matching posts.
        :param hazard_type: The type of hazard to look for.
        :return: A list of posts that meet the given criteria.
        """
        matching_posts = Posts.objects.filter(hazard_type__hazard_name__exact=hazard_type)
        return matching_posts

    @staticmethod
    def search_by_description(query):
        """
        Given a query, returns a set of matching posts.
        :param query: A string to search the post body for.
        :return: A list of posts that meet the given criteria.
        """
        matching_posts = Posts.objects.filter(description__icontains=query)
        return matching_posts

    def get_userdata(self):
        """
        Returns the UserData object for the author of the given post.
        :return: UserData
        """
        return UserData.objects.get(username_id=self.user_id)

    def __str__(self):
        """
        Returns the string representation of a post for easy reading in the shell.
        :return: The string representation of the current post.
        """
        return str(self.post_id)


class PostImageCollection(models.Model):
    """
    Table to separate images from the post for database table decoupling.
    """
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
        """
        Returns the string representation of this class.
        :return: a string representation of this class.
        """
        return self.messages

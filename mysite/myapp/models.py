from django.db import models

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

"""
Users:
    user_id - INT, Primary Key, Auto Increment
    username - VARCHAR(255)
    email - VARCHAR(255)
    password - VARCHAR(255)
    type - VARCHAR(255)
    strikes - INT
By default, there will be a field called "id" which will auto increment
You can define any field as auto increment using AutoField field.
Type is a reserved word in Python. Changes to user_type.
"""


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    user_type = models.CharField(max_length=255)
    strikes = models.IntegerField()


"""
User_data
    user_id - INT, Primary Key
    first_name - VARCHAR(255)
    last_name - VARCHAR(255)
    biography - TEXT
"""


class UserData(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE())
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    biography = models.CharField(max_length=400)


"""
Posts: 
    post_id - INT, Primary Key, Auto Increment
    user_id - INT
    location - VARCHAR(255)
    description - TEXT
    date - DATE
    comments - TEXT
    reports - TEXT
"""


class Posts(models.Model):
    post_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE())
    location = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date = models.DateTimeField()
    comments = models.CharField(max_length=255)
    reports = models.CharField(max_length=255)


"""
Locations: 
    location_id - INT, Primary Key
    location_name - VARCHAR(255)
"""


class Locations(models.Model):
    location_id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=255)


"""
Messages:
    user_id1 - INT
    user_id2 - INT
    messages - TEXT
    Dates - DATETIME
"""


class Messages(models.Model):
    user_id1 = models.ForeignKey(Users)
    user_id2 = models.ForeignKey(Users)
    messages = models.CharField(max_length=400)
    dates = models.DateTimeField()
# Generated by Django 2.0.3 on 2018-04-02 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_userdata_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdata',
            old_name='user_id',
            new_name='username',
        ),
    ]
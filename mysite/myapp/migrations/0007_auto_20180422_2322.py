# Generated by Django 2.0.3 on 2018-04-23 06:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20180401_2219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='image',
        ),
        migrations.AddField(
            model_name='posts',
            name='image1',
            field=models.ImageField(null=True, upload_to=myapp.models.post_directory_path),
        ),
        migrations.AddField(
            model_name='posts',
            name='image2',
            field=models.ImageField(null=True, upload_to=myapp.models.post_directory_path),
        ),
        migrations.AddField(
            model_name='posts',
            name='image3',
            field=models.ImageField(null=True, upload_to=myapp.models.post_directory_path),
        ),
        migrations.AddField(
            model_name='posts',
            name='image4',
            field=models.ImageField(null=True, upload_to=myapp.models.post_directory_path),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='avatar',
            field=models.ImageField(null=True, upload_to=myapp.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='biography',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='location',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL),
        ),
    ]

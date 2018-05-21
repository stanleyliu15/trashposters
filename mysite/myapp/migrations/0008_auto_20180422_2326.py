# Generated by Django 2.0.3 on 2018-04-23 06:26

from django.db import migrations, models
import django.db.models.deletion
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20180422_2322'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostImageCollection',
            fields=[
                ('post_image_collection_id', models.AutoField(primary_key=True, serialize=False)),
                ('image1', models.ImageField(null=True, upload_to=myapp.models.post_directory_path)),
                ('image2', models.ImageField(null=True, upload_to=myapp.models.post_directory_path)),
                ('image3', models.ImageField(null=True, upload_to=myapp.models.post_directory_path)),
                ('image4', models.ImageField(null=True, upload_to=myapp.models.post_directory_path)),
            ],
        ),
        migrations.RemoveField(
            model_name='posts',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='image4',
        ),
        migrations.AddField(
            model_name='postimagecollection',
            name='post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Posts'),
        ),
    ]

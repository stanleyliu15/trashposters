# Generated by Django 2.0.3 on 2018-04-01 07:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment_body', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DummyTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Water makes the frogs turn gay.', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='HazardType',
            fields=[
                ('hazard_id', models.AutoField(default='Trash', primary_key=True, serialize=False)),
                ('hazard_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
                ('location_name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=32)),
                ('address', models.CharField(max_length=255)),
                ('zip_code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messages', models.CharField(max_length=400)),
                ('dates', models.DateTimeField()),
                ('user_id1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_userid1', to=settings.AUTH_USER_MODEL)),
                ('user_id2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_userid2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=400)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('hazard_type', models.ForeignKey(on_delete=None, to='myapp.HazardType')),
                ('location', models.ForeignKey(on_delete=None, to='myapp.Location')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biography', models.CharField(max_length=400)),
                ('location', models.ForeignKey(on_delete=None, to='myapp.Location')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comments',
            name='post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Posts'),
        ),
        migrations.AddField(
            model_name='comments',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

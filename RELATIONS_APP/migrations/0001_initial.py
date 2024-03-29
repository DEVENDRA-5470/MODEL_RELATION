# Generated by Django 4.2.9 on 2024-02-27 11:42

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
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_img', models.ImageField(blank=True, default='media/default.jpg', null=True, upload_to='pics')),
                ('name', models.CharField(default='Hey , (Default)', max_length=200, null=True)),
                ('title', models.CharField(default='This is the default, title change it in profile.', max_length=200, null=True)),
                ('desc', models.CharField(default='Hey, there this is a default text description about you that you can change on after clicking on "Edit" or going to your profile page.', max_length=200, null=True)),
                ('instagram', models.URLField(default='Profile Link', null=True)),
                ('github', models.URLField(default='Profile Link', null=True)),
                ('linkedin', models.URLField(default='Profile Link', null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('published_date', models.DateField()),
                ('content', models.TextField()),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='RELATIONS_APP.author')),
            ],
            options={
                'ordering': ['-published_date'],
            },
        ),
    ]

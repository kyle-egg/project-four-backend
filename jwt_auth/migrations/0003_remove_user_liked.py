# Generated by Django 3.2.7 on 2021-09-09 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jwt_auth', '0002_user_liked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='liked',
        ),
    ]
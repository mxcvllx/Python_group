# Generated by Django 4.2.1 on 2023-05-24 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_auth_provider'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='auth_provider',
        ),
    ]

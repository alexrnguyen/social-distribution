# Generated by Django 5.0.2 on 2024-02-24 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0008_remove_follower_is_friend'),
    ]

    operations = [
        migrations.AddField(
            model_name='follower',
            name='is_friend',
            field=models.BooleanField(default=False),
        ),
    ]

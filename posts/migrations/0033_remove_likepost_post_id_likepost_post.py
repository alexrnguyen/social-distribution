# Generated by Django 5.0.2 on 2024-03-18 16:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0032_remove_comment_name_remove_likepost_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likepost',
            name='post_id',
        ),
        migrations.AddField(
            model_name='likepost',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Likeddddd', to='posts.post'),
        ),
    ]

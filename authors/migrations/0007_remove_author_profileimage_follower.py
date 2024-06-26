# Generated by Django 5.0.2 on 2024-02-24 06:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0006_rename_url_author_profile_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='profileImage',
        ),
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_accepted', models.BooleanField(default=False)),
                ('is_friend', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='authors.author')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to='authors.author')),
            ],
            options={
                'unique_together': {('author_id', 'follower_id')},
            },
        ),
    ]

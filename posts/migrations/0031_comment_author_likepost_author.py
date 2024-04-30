# Generated by Django 5.0.2 on 2024-03-17 05:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0040_node_is_active'),
        ('posts', '0030_notification_notification_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='authors.author'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='likepost',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='authors.author'),
            preserve_default=False,
        ),
    ]
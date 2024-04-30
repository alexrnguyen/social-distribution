# Generated by Django 5.0.2 on 2024-02-26 10:36

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0018_alter_author_host_alter_author_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='host',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='author',
            name='uuid',
            field=models.CharField(default=uuid.UUID('55a684c4-ca05-45c2-89f6-f0b6c3b800d2'), editable=False, max_length=50, unique=True),
        ),
    ]

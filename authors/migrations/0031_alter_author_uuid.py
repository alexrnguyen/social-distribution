# Generated by Django 5.0.2 on 2024-02-28 03:38

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0030_alter_author_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='uuid',
            field=models.CharField(default=uuid.UUID('3d47111f-79f4-496e-9bae-5ac9ee938db3'), editable=False, max_length=50, unique=True),
        ),
    ]

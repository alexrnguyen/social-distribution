# Generated by Django 5.0.2 on 2024-02-28 03:25

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0026_alter_author_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='uuid',
            field=models.CharField(default=uuid.UUID('6add12ca-d0ab-40f7-84cc-300f71ab16c4'), editable=False, max_length=50, unique=True),
        ),
    ]

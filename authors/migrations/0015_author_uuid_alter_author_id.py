# Generated by Django 5.0.2 on 2024-02-25 21:58

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0014_remove_author_uuid_alter_author_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='uuid',
            field=models.CharField(default=uuid.UUID('78a8e131-b5fe-496b-9185-935e2e3d4609'), editable=False, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

# Generated by Django 5.0.2 on 2024-02-25 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0013_author_uuid_alter_author_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='uuid',
        ),
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.IntegerField(editable=False, primary_key=True, serialize=False),
        ),
    ]

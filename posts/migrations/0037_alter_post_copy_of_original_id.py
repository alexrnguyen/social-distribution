# Generated by Django 5.0.2 on 2024-03-24 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0036_alter_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='copy_of_original_id',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

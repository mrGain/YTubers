# Generated by Django 4.0.1 on 2022-02-10 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0003_alter_youtuber_camera_type_alter_youtuber_categoty_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='youtuber',
            old_name='categoty',
            new_name='category',
        ),
    ]

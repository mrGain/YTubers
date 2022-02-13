# Generated by Django 4.0.1 on 2022-02-10 06:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0002_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='youtube_link',
            field=models.CharField(default=django.utils.timezone.now, max_length=225),
            preserve_default=False,
        ),
    ]
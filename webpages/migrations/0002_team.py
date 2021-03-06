# Generated by Django 4.0.1 on 2022-02-09 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=100)),
                ('fb_link', models.CharField(max_length=225)),
                ('insta_link', models.CharField(max_length=225)),
                ('photo', models.ImageField(upload_to='media/team/%Y/%m/%d/')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

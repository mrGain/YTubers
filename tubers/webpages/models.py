
from django.db import models


# Create your models here.

class Team(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=100)
    fb_link = models.CharField(max_length=225)
    insta_link = models.CharField(max_length=225)
    youtube_link = models.CharField(max_length=225)
    photo = models.ImageField(upload_to='media/team/%Y/%m/%d/')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class Slider(models.Model):
    headline = models.CharField(max_length=225)
    subtitle = models.CharField(max_length=225)
    button_text = models.CharField(max_length=225)
    photo = models.ImageField(upload_to='media/slider/%Y/')
    created_date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.headline

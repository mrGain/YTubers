from random import choice
from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.
class Youtuber(models.Model):

    crew_choices = [
        ('solo', 'solo'),
        ('small', 'small'),
        ('large', 'large'),
    ]
    camera_choices = [
        ('canon', 'canon'),
        ('nikon', 'nikon'),
        ('sony', 'sony'),
        ('fuji', 'fuji'),
        ('red', 'red'),
        ('penasonic', 'penasonic'),
        ('other', 'other'),
    ]
    category_choices = [
        ('code', 'code'),
        ('mobile_review', 'mobile_review'),
        ('gagets_review', 'gagets_review'),
        ('vlogs', 'vlogs'),
        ('comedy', 'comedy'),
        ('film_making', 'film_making'),
        ('gaming', 'gaming'),
        ('cooking', 'cooking'),
    ]


    name = models.CharField(max_length=225)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='media/ytubers/%Y/%m/')
    video_url = models.CharField(max_length=225)
    description = RichTextField()
    city = models.CharField(max_length=100)
    age = models.IntegerField()
    height = models.IntegerField()
    crew = models.CharField(choices=crew_choices,max_length=225)
    camera_type = models.CharField(choices=camera_choices,max_length=225)
    subs_count = models.CharField(max_length=225)
    category = models.CharField(choices=category_choices,max_length=225)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now ,blank=True)

    def __str__(self):
        return self.name

    

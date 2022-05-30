from django.contrib import admin
from django.utils.html import format_html
from .models import Youtuber




class YoutuberAdmin(admin.ModelAdmin):
    def myphoto(self ,object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))

    list_display = ['id','name','myphoto','category','subs_count','is_featured']
    search_fields = ['name','category','camera_type']
    list_filter = ['category','city']
    list_display_links = ['id','name']
    list_editable = ['is_featured']

# Register your models here.
admin.site.register(Youtuber,YoutuberAdmin)
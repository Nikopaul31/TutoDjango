from django.contrib import admin
from appone.models import Song, Album


class AlbumAdmin(admin.ModelAdmin):
    fields = ('name', )


admin.site.register(Album, AlbumAdmin)
admin.site.register(Song)

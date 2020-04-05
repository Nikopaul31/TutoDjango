from django.http import HttpResponse
from django.shortcuts import render

from appone.models import Song


def song_list(request):
    names=[]
    for s in Song.objects.all():
        names.append(s.name)
    body = '</br>'.join(names)
    return HttpResponse(body)


def add_song(request, song_name, song_duration):
    song = Song(name=song_name, duration=song_duration)
    song.save()
    return HttpResponse("Song saved with id : {}".format(song.pk))

from django.shortcuts import render

from modelform.forms import SongForm

def song_create(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        form.save()
        # instance accede a l'instance du model que l'on vient de créer
        print(form.instance)

    else:
        form = SongForm()
    return render(request, 'modelform/song_create.html', {'form': form})

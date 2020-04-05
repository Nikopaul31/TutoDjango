from django.http import HttpResponse
from django.shortcuts import render

from PyRPG.forms import PlayerForm
from PyRPG.models import Region


def player_create(request, region_id):

    # if Region.objects.filter(pk=region_id):
    #
    #     if request.method == 'POST':
    #         form = PlayerForm(request.POST)
    #         player = form.save(commit=False)
    #         # instance accede a l'instance du modele que l'on vient de créer
    #         player.region = region_id
    #         player.save()
    #         print(form.instance)
    #
    #     else:
    #         form = PlayerForm()
    #
    #     return render(request, 'PyRPG/player_create.html', {'form': form})
    #
    # else:
    #
    #     return HttpResponse("Region does not exists")

    ##################CORRECTION##################
    try:
        region = Region.objects.get(pk=region_id)
    except Region.DoesNotExist:
        # return HttpResponse("Region {} does not exist".format(region_id))
        region = Region(pk=region_id)
        errors = 'Invalid region, cannot create player'

    if request.method == 'POST':
        form = PlayerForm(request.POST)

        if form.is_valid():
            player = form.save(commit=False)
            player.region=region
            player.save()

            print(player)

    else:
        form = PlayerForm()

    context = {
        'form': form,
        'region': region,
        'errors': errors,
    }

    return render(request, 'PyRPG/player_create.html', context)




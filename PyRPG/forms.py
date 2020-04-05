from django import forms

from PyRPG.models import Player


class PlayerForm(forms.ModelForm):
    # pour rattacher le model au modelForm il faut definir la classe meta avec les données que l on veut
    class Meta:
        # defini la classe a associer
        model = Player

        # defini les champs visible, ici on affiche que le name et la duration:
        # fields = ['name', 'duration']

        # si on veut tout afficher sauf la region:
        exclude = ['region']

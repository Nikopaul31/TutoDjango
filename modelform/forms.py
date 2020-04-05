from django import forms

from modelform.models import Song


class SongForm(forms.ModelForm):
    # pour rattacher le model au modelForm il faut definir la classe meta avec les données que l on veut
    class Meta:
        # defini la classe a associer
        model = Song

        # defini les champs visible, ici on affiche que le name et la duration:
        # fields = ['name', 'duration']

        # si on veut tout afficher :
        fields = '__all__'
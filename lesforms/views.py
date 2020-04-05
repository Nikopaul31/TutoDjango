from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from lesforms.forms import TestForm

def thanks(request):
    return HttpResponse('Thanks, your form has been processed')

def get_form_data(request):

    # si l'on effecue un POST, c'est a dire si l'on submit
    if request.method == 'POST':
        print('In POST processing')
        # request.POST contient toutes les cles et les valeurs contenues dans le formulaire
        form = TestForm(request.POST)

        if form.is_valid():
            print('name:', form.cleaned_data['name'])
            print('email:', form.cleaned_data['email'])
            print('yes_no:', form.cleaned_data['yes_no'])
            print('city:', form.cleaned_data['city'])

            # redirige sur la page 'thanks' défini dans URL afin de ne pas revenir sur la meme page
            return HttpResponseRedirect(reverse('thanks'))

    # sinon on a juste acceder a la page
    else:
        form = TestForm()
    return render(request, 'lesforms/form.html', {'form': form})

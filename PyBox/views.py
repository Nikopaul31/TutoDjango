from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from PyBox.forms import TestForm


def thanks(request, clean_name):
    return HttpResponse('Thanks {}, your form has been processed'.format(clean_name))


def get_form_data(request):

    # si l'on effecue un POST, c'est a dire si l'on submit
    if request.method == 'POST':
        print('In POST processing')
        # request.POST contient toutes les cles et les valeurs contenues dans le formulaire
        form = TestForm(request.POST)

        if form.is_valid():
            print('name:', form.cleaned_data['name'])
            print('email:', form.cleaned_data['email'])
            print('signup_to_newsletter:', form.cleaned_data['signup_to_newsletter'])
            print('plan:', form.cleaned_data['plan'])
            print('additonnal option:', form.cleaned_data['additional_options'])

            clean_name = form.cleaned_data['name']

            if form.cleaned_data['signup_to_newsletter']:
                print('you registered to newsletter with email : {} '.format(form.cleaned_data['email']))

            # redirige sur la page 'thanks' défini dans URL afin de ne pas revenir sur la meme page
            return HttpResponseRedirect(reverse('thanksPybox', args=[clean_name]))

    # sinon on accede a la page de formulaire avec les champs vides
    else:
        form = TestForm()
    return render(request, 'pybox/form.html', {'form': form})

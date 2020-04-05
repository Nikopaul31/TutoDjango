from django.shortcuts import render
# permete de retourner une repose compréhensible par le navigateur
from django.http import HttpResponse

# permet de charger un template
from django.template import loader

from peoplebookapp.peoples import peoples


# Create your views here.
def hello(request):
    return HttpResponse("hello from peoplebookapp view !")

def showAllUsers(request):
    # retourne la liste de tous les utilisateurs
    return HttpResponse("liste des utilisateurs")


def showUserDetail(request, name):
    # charge le template index.html present dans le sous dossier peoplebookapp present dans templates present dans peoplebookapp
    template = loader.get_template('peoplebookapp/indexImage.html')


    # le contexte est l'ensemble des variables que l'on fournira aux template afin de le dynamiser
    context = {
        'pictures': [
            {
                'name': 'han',
                'filename': 'han.jpg',
            },
            {
                'name': 'chewbacca',
                'filename': 'chewbacca.jpg',
            },
            {
                'name': 'c3po',
                'filename': 'c3po.jpg',
            },
            {
                'name': 'r2d2',
                'filename': 'r2d2.jpg',
            },
        ],
    }

    # render permet d'injecter le contexte (dictionnaire)
    return HttpResponse(template.render(context, request))


def showUsers(request, display="small"):
    context = {
        'display': display,
        'users': peoples
    }
    return render(request, 'peoplebookapp/users_list.html', context)

def showUserDetail2(request, name):
    context = {
        'user': peoples[name]
    }
    return render(request, 'peoplebookapp/users_detail.html', context)

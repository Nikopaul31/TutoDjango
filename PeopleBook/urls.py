"""PeopleBook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from appone import views as apponeviews
from lesforms import views as lesformsviews
from myDevices import views as deviceViews
from PyPyMusic.admin import admin_site
from PyBox import views as Pyboxviews
from modelform import views as modelformviews
from PyRPG import views as PyRPGviews

urlpatterns = [
    path('admin/', admin_site.urls),

    path('songs/', apponeviews.song_list),
    path('songs/add/<str:song_name>/<int:song_duration>/', apponeviews.add_song),
    # include permet d'inserer les urls contenu dans peoplebookapp.urls

    path('peoplebook/', include('peoplebookapp.urls')),

    path('devices/<int:id>/', deviceViews.device_detail),
    path('devices/add/<str:device_os>/<str:device_model>/', deviceViews.add_device),
    path('devices/filter/<str:device_os>/', deviceViews.filter_devices),

    path('getformdata/', lesformsviews.get_form_data, name='get-form-data'),
    path('thanks/', lesformsviews.thanks, name='thanks'),

    path('register/', Pyboxviews.get_form_data, name='pybox-get-form-data'),
    path('thanksPybox/<str:clean_name>', Pyboxviews.thanks, name='thanksPybox'),

    path('player/registration/<int:region_id>', PyRPGviews.player_create, name='player-registration')


]

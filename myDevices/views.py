from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from myDevices.models import Device


def device_detail(request, id):

    try:
        obj2 = get_object_or_404(Device, pk=id)
        context = {
            'device': obj2,
        }
        return render(request, 'myDevices/device_detail_page.html', context)

    except Device.DoesNotExist:
        return HttpResponse(status=404)


def add_device(request, device_os, device_model):
    device = Device(os=device_os, model=device_model)
    device.save()
    return HttpResponse("device {} added".format(device.pk))


def filter_devices(request, device_os):
    devices = Device.objects.filter(os__exact=device_os).values()
    # print("resultat du filtre :")
    # print(devices)
    context = {
        'devices': devices
    }
    return render(request, 'myDevices/filter_page.html', context)

    #########CORRECTION##############

    # devices_names=[]

    # for d in Device.objects.filter(os__exact=device_os):
    #     devices_names.append(d)
    #
    # body = '<br/>.join(devices_names)'

    # return HttpResponse(body)

    #################################

from django.shortcuts import render

from django.views import generic

from .models import CompanyService, ServiceCategory, Driver, Transport


def index(request):
    service_list = CompanyService.objects.all()
    return render(request, 'index.html', context={'service_list': service_list})


def services_list(request):
    service_list = CompanyService.objects.all()
    return render(request, 'companyservice_list.html', context={'service_list': service_list})


def drivers_list(request):
    lst = Driver.objects.all()
    return render(request, 'drivers_list.html', context={'drivers_list': lst})


def transport_list(request):
    lst = Transport.objects.all()
    return render(request, 'transport_list.html', context={'transport_list': lst})

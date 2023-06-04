from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
import datetime



from django.views import generic

from .models import CompanyService, ServiceCategory, Driver, Transport, Order, Cargo


def index(request):
    service_list = CompanyService.objects.all()
    return render(request, 'index.html', context={'service_list': service_list})


def services_list(request):
    service_list = CompanyService.objects.all()
    transport_list = Transport.objects.all()
    drivers_list = Driver.objects.all()
    return render(request, 'companyservice_list.html',
                  context={'service_list': service_list, 'transport_list': transport_list, 'drivers_list': drivers_list})


def drivers_list(request):
    lst = Driver.objects.all()
    return render(request, 'drivers_list.html', context={'drivers_list': lst})


def transport_list(request):
    lst = Transport.objects.all()
    return render(request, 'transport_list.html', context={'transport_list': lst})

def orders_list(request):
    lst = Order.objects.all()
    return render(request, 'orders_list.html', context={'orders_list': lst})


def create_order(request):
    if request.method == "POST":
        order = Order()
        order.date = datetime.date.today()

        driver_pk = request.POST.get("driver")
        order.driver = Driver.objects.get(pk=driver_pk)

        order.client = request.POST.get("client")

        cargo_name = request.POST.get("cargo")
        order.cargo = Cargo()
        order.cargo.name = cargo_name
        order.cargo.save()

        transport_pk = request.POST.get("transport")
        order.transport = Transport.objects.get(pk=transport_pk)

        order.service = request.POST.get("service")
        # order.cost = order.service.cost

        order.save()
    return HttpResponseRedirect("/")



from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic

from .forms import TransportForm
from .models import CompanyService, ServiceCategory, Driver, Transport, Order, Cargo, TransportType, BodyType


def index(request):
    service_list = CompanyService.objects.all()
    return render(request, 'index.html', context={'service_list': service_list})


def services_list(request):
    service_list = CompanyService.objects.all()
    transport_list = Transport.objects.all()
    drivers_list = Driver.objects.all()
    return render(request, 'order/companyservice_list.html',
                  context={'service_list': service_list, 'transport_list': transport_list, 'drivers_list': drivers_list})


# return only drivers
def drivers_list(request):
    lst = Driver.objects.all()
    return render(request, 'order/drivers_list.html', context={'drivers_list': lst})

def createtransport_page(request):
    return render(request, 'order/createtransport_page.html', context={})


def transport_list(request):
    lst = Transport.objects.all()
    return render(request, 'transport/transport_list.html', context={'transport_list': lst})


def transport_type_list(request):
    lst = TransportType.objects.all()
    return render(request, 'order/createtransport_page.html', context={'transport_type_list': lst})


def body_type_list(request):
    lst = BodyType.objects.all()
    return render(request, 'order/createtransport_page.html', context={'body_type_list': lst})

@login_required
def orders_list(request):
    lst = Order.objects.all()
    return render(request, 'order/orders_list.html', context={'orders_list': lst})


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


# def create_transport(request):
#     if request.method == "POST":
#         transport = Transport()
#         transport.name = request.POST.get("name")
#
#         transport_type_pk = request.POST.get("type")
#         transport.type = TransportType.objects.get(pk=transport_type_pk)
#
#         body_type_pk = request.POST.get("body_type")
#         transport.type = BodyType.objects.get(pk=body_type_pk)
#         transport.save()
#     return HttpResponseRedirect("/home/transport")

def create_transport(request):
    if request.method == 'POST':
        form = TransportForm(request.POST, request.FILES)
        if form.is_valid():
            transport = form.save()
            return redirect('/home/transport/', pk=transport.pk)
    else:
        form = TransportForm()
    return render(request, 'transport/create.html', {'form': form})

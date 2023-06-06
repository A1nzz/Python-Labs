
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.decorators import login_required, permission_required


from .forms import TransportForm, CargoForm, ClientForm, ServiceForm
from .models import CompanyService, ServiceCategory, Driver, Transport, Order, Cargo, TransportType, BodyType, Client,\
    CargoType


def index(request):
    service_list = CompanyService.objects.all()
    return render(request, 'index.html', context={'service_list': service_list})


# return only drivers
def drivers_list(request):
    lst = Driver.objects.exclude(is_staff=True)
    return render(request, 'order/drivers_list.html', context={'drivers_list': lst})


def body_type_list(request):
    lst = BodyType.objects.all()
    return render(request, 'order/createtransport_page.html', context={'body_type_list': lst})


@login_required
def orders_list(request):
    lst = Order.objects.all()
    user = request.user
    if user.is_staff:
        return render(request, 'order/orders_list.html', context={'orders_list': lst})
    else:
        lst = Order.objects.filter(driver=user)
        return render(request, 'order/orders_list.html', context={'orders_list': lst})


def create_user_order(request):
    if request.method == "POST":
        order = Order()
        order.date = datetime.date.today()

        driver_pk = request.POST.get("driver")
        order.driver = Driver.objects.get(pk=driver_pk)

        client_email = request.POST.get("client")
        if Client.objects.filter(email=client_email).exists():
            order.client = Client.objects.get(email=client_email)
        else:
            client = Client()
            client.email = client_email
            client.first_name = "user"
            client.last_name = "user"
            order.client = client
        order.client.save()

        cargo_name = request.POST.get("cargo")
        if Cargo.objects.filter(name=cargo_name).exists():
            order.cargo = Cargo.objects.get(name=cargo_name)
        else:
            cargo_type_pk = request.POST.get("cargo_type")
            cargo_type = CargoType.objects.get(pk=cargo_type_pk)
            order.cargo = Cargo()
            order.cargo.name = cargo_name
            order.cargo.type = cargo_type

        order.cargo.save()

        transport_pk = request.POST.get("transport")
        order.transport = Transport.objects.get(pk=transport_pk)

        order.service = CompanyService.objects.get(pk=request.POST.get("service"))
        order.cost = order.service.cost

        order.save()
    return HttpResponseRedirect("/")


@login_required
@permission_required('order.add_transport', raise_exception=True)
def create_transport(request):
    if request.method == 'POST':
        form = TransportForm(request.POST, request.FILES)
        if form.is_valid():
            transport = form.save()
            return redirect('/home/transport/', pk=transport.pk)
    else:
        form = TransportForm()
    return render(request, 'transport/create.html', {'form': form})


def transport_list(request):
    lst = Transport.objects.all()
    return render(request, 'transport/transport_list.html', context={'transport_list': lst})


@login_required
@permission_required('order.change_transport', raise_exception=True)
def edit_transport(request, id):
    transport = get_object_or_404(Transport, id=id)
    if request.method == 'POST':
        form = TransportForm(request.POST, instance=transport)
        if form.is_valid():
            form.save()
            return redirect('transport')
    else:
        form = TransportForm(instance=transport)
    return render(request, 'transport/create.html', {'form': form})


@login_required
@permission_required('order.delete_transport', raise_exception=True)
def delete_transport(request, id):
    transport = Transport.objects.get(id=id)
    transport.delete()
    return redirect('transport')


@login_required
def cargos_list(request):
    lst = Cargo.objects.all()
    return render(request, 'cargos/cargos_list.html', context={'cargos_list': lst})


@login_required
@permission_required('order.add_cargo', raise_exception=True)
def create_cargo(request):
    if request.method == 'POST':
        form = CargoForm(request.POST, request.FILES)
        if form.is_valid():
            cargo = form.save()
            return redirect('/home/cargo/', pk=cargo.pk)
    else:
        form = CargoForm()
    return render(request, 'cargos/create.html', {'form': form})


@login_required
@permission_required('order.change_cargo', raise_exception=True)
def edit_cargo(request, id):
    cargo = get_object_or_404(Cargo, id=id)
    if request.method == 'POST':
        form = CargoForm(request.POST, instance=cargo)
        if form.is_valid():
            form.save()
            return redirect('cargos_list')
    else:
        form = CargoForm(instance=cargo)
    return render(request, 'cargos/create.html', {'form': form})


@login_required
@permission_required('order.delete_cargo', raise_exception=True)
def delete_cargo(request, id):
    cargo = Cargo.objects.get(id=id)
    cargo.delete()
    return redirect('cargos_list')


@login_required
def clients_list(request):
    lst = Client.objects.all()
    return render(request, 'clients/clients_list.html', context={'clients_list': lst})


@login_required
@permission_required('order.add_client', raise_exception=True)
def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            client = form.save()
            return redirect('/home/clients/', pk=client.pk)
    else:
        form = ClientForm()
    return render(request, 'clients/create.html', {'form': form})


@login_required
@permission_required('order.change_client', raise_exception=True)
def edit_client(request, id):
    client = get_object_or_404(Client, id=id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('clients_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'clients/create.html', {'form': form})


@login_required
@permission_required('order.delete_client', raise_exception=True)
def delete_client(request, id):
    client = Client.objects.get(id=id)
    client.delete()
    return redirect('clients_list')


def services_list(request):
    transport_list = Transport.objects.all()
    drivers_list = Driver.objects.exclude(is_staff=True)
    cargo_types_list = CargoType.objects.all()
    category = request.GET.get('category', '')
    min_price = request.GET.get('min_price', '')
    max_price = request.GET.get('max_price', '')
    sort = request.GET.get('sort', '')

    service_list = CompanyService.objects.all()
    if category:
        service_list = service_list.filter(category__name=category)
    if min_price:
        service_list = service_list.filter(cost__gte=min_price)
    if max_price:
        service_list = service_list.filter(cost__lte=max_price)

    if sort == 'asc':
        service_list = service_list.order_by('cost')
    elif sort == 'desc':
        service_list = service_list.order_by('-cost')
    categories = ServiceCategory.objects.all()

    return render(request, 'services/companyservice_list.html', context={'service_list': service_list,
                                                                         'category ': category,
                                                                         'min_price': min_price,
                                                                         'max_price': max_price,
                                                                         'categories': categories,
                                                                         'transport_list': transport_list,
                                                                         'drivers_list': drivers_list,
                                                                         'cargo_types_list': cargo_types_list})


@login_required
@permission_required('order.add_client', raise_exception=True)
def create_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save()
            return redirect('/home/services/', pk=service.pk)
    else:
        form = ServiceForm()
    return render(request, 'services/create.html', {'form': form})


def edit_service(request, id):
    service = get_object_or_404(CompanyService, id=id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('services')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'services/create.html', {'form': form})


@login_required
@permission_required('order.delete_client', raise_exception=True)
def delete_service(request, id):
    service = CompanyService.objects.get(id=id)
    service.delete()
    return redirect('services')

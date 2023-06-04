from django.contrib import admin

from order.models import Transport, TransportType, BodyType, \
    Cargo, CargoType, Order, ServiceCategory, CompanyService,\
    Driver, Client


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'age')
    fields = [('last_name', 'first_name'), 'age']


@admin.register(Transport)
class TransportAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'body_type')


class TransportInline(admin.TabularInline):
    model = Transport


@admin.register(TransportType)
class TransportTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [TransportInline]


@admin.register(BodyType)
class BodyTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [TransportInline]


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')


class CargoInline(admin.TabularInline):
    model = Cargo


@admin.register(CargoType)
class CargoTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [CargoInline]


@admin.register(CompanyService)
class CompanyServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'cost']
    list_filter = ['category']


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('date', 'client', 'driver', 'transport', 'cost', 'cargo', 'service')


admin.site.register(Client)

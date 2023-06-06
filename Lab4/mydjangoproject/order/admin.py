from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model


from order.models import Transport, TransportType, BodyType, \
    Cargo, CargoType, Order, ServiceCategory, CompanyService,\
    Driver, Client


class DriverCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Driver
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'date_of_birth', 'phone_number', 'groups')

class DriverChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Driver
        fields = ('username', 'first_name', 'last_name', 'email', 'date_of_birth', 'phone_number', 'groups')

class DriverAdmin(UserAdmin):
    form = DriverChangeForm
    add_form = DriverCreationForm

    list_display = ('username', 'first_name', 'last_name', 'email', 'date_of_birth', 'phone_number')
    list_filter = ('date_of_birth', 'email', 'groups')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'date_of_birth', 'phone_number', 'groups'),
        }),
    )

admin.site.register(Driver, DriverAdmin)
admin.site.unregister(Group)



# admin.site.register(get_user_model())
# class CustomUserAdmin(UserAdmin):
#
#     model = Driver
#     list_display = ('email', 'last_name', 'first_name',)
#     list_filter = ('email', 'is_staff', 'is_active',)
#     filter_horizontal = ('groups', 'user_permissions',)
#
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Permissions', {'fields': ('is_staff', 'is_active')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('first_name', 'last_name', 'email', 'password1', 'password2', 'is_staff', 'is_active',  'phone_number', 'date_of_birth')}
#         ),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)
#
#
# admin.site.register(Driver, CustomUserAdmin)


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

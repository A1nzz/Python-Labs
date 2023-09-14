from datetime import date
import phonenumbers


from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from order.models import Transport, TransportType, BodyType, \
    Cargo, CargoType, Order, ServiceCategory, CompanyService,\
    Driver, Client, Post, Faq, Coupon


class DriverCreationForm(UserCreationForm):
    phone_number = forms.CharField(label=('Phone number'), max_length=15)

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number:
            try:
                parsed_number = phonenumbers.parse(phone_number, None)
                if not phonenumbers.is_valid_number(parsed_number):
                    raise ValidationError(('Invalid phone number format.'))
            except phonenumbers.phonenumberutil.NumberParseException:
                raise ValidationError(('Invalid phone number format.'))
        return phone_number

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')
        if date_of_birth:
            today = date.today()
            age = today.year - date_of_birth.year
            if today.month < date_of_birth.month or (
                    today.month == date_of_birth.month and today.day < date_of_birth.day):
                age -= 1
            if age < 18:
                raise ValidationError("Водитель должен быть старше 18 лет для регистрации.")
        return date_of_birth

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

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ['question']


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Client)

from django import forms

from order.models import Transport, Cargo, Client, CompanyService


class TransportForm(forms.ModelForm):
    class Meta:
        model = Transport
        fields = "__all__"


class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = "__all__"


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"


class ServiceForm(forms.ModelForm):
    class Meta:
        model = CompanyService
        fields = "__all__"

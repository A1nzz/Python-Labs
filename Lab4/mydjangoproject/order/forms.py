from django import forms

from order.models import Transport


class TransportForm(forms.ModelForm):
    class Meta:
        model = Transport
        fields = "__all__"

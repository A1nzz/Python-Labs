from django import forms

from order.models import Transport, Cargo, Client, CompanyService, Review


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


class ReviewForm(forms.ModelForm):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            client = Client.objects.get(email=email)
            self.instance.client = client
        except Client.DoesNotExist:
            raise forms.ValidationError('Клиент с такой почтой не существует.')
        return email

    class Meta:
        model = Review
        fields = ['email', 'rating', 'text']
from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns


# Create your models here.
class Driver(models.Model):
    """"
    Модель для водителя
    """
    first_name = models.CharField(max_length=255, blank=False)

    last_name = models.CharField(max_length=255, blank=False)

    age = models.PositiveIntegerField()

    transport = models.OneToOneField('Transport', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('driver-detail', args=[str(self.id)])


class Transport(models.Model):
    """Модель для транспорта"""
    name = models.CharField(max_length=255, blank=False)

    type = models.ForeignKey('TransportType', on_delete=models.SET_NULL, null=True)

    bodyType = models.ForeignKey('BodyType', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.name}'


class TransportType(models.Model):
    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return f'{self.name}'


class BodyType(models.Model):
    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return f'{self.name}'


class Client(models.Model):
    first_name = models.CharField(max_length=255, blank=False)

    last_name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Cargo(models.Model):
    name = models.CharField(max_length=255, blank=False)

    type = models.ForeignKey('CargoType', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.name}'


class CargoType(models.Model):
    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    company = models.ForeignKey('TransportCompany', on_delete=models.SET_NULL, null=True)

    driver = models.ForeignKey('Driver', on_delete=models.SET_NULL, null=True)

    client = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True)

    cargo = models.ForeignKey('Cargo', on_delete=models.SET_NULL, null=True)

    cost = models.DecimalField(default=0, decimal_places=2, max_digits=30)

    date = models.DateField()

    def __str__(self):
        return f'{self.date} driver: {self.driver} client: {self.client}'


class TransportCompany(models.Model):
    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return f'{self.name}'


class CompanyService(models.Model):
    name = models.CharField(max_length=255, blank=False)

    company = models.ForeignKey('TransportCompany', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.name}'



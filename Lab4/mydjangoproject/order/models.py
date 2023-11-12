from datetime import date
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, date_of_birth, phone_number, password=None, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name,
                          date_of_birth=date_of_birth, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email='', first_name='', last_name='', date_of_birth='2000-10-10', phone_number='+375 (29) 123-45-67', password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser is_staff must be True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser is_superuser must be True.')

        return self.create_user(email, first_name, last_name, date_of_birth, phone_number, password, **extra_fields)


# Create your models here.
class Driver(AbstractUser):
    """"
    Модель для водителя
    """
    first_name = models.CharField(max_length=255, blank=False)

    last_name = models.CharField(max_length=255, blank=False)

    date_of_birth = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    groups = models.ManyToManyField('auth.Group', related_name='drivers', blank=True)

    @property
    def age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        if today.month < self.date_of_birth.month or (
                today.month == self.date_of_birth.month and today.day < self.date_of_birth.day):
            age -= 1
        return age

    REQUIRED_FIELDS = ['first_name', 'last_name',
                       'email', 'date_of_birth', 'phone_number']
    USERNAME_FIELD = 'username'
    objects = MyUserManager()

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return f'{self.first_name} {self.last_name} {self.email}'


class Transport(models.Model):
    """Модель для транспорта"""
    name = models.CharField(max_length=255, blank=False)

    type = models.ForeignKey('TransportType', on_delete=models.CASCADE, null=True)

    body_type = models.ForeignKey('BodyType', on_delete=models.CASCADE, null=True)

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

    email = models.EmailField(max_length=255, blank=False, default="")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Cargo(models.Model):
    name = models.CharField(max_length=255, blank=False)

    type = models.ForeignKey('CargoType', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.name}'


class CargoType(models.Model):
    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):

    driver = models.ForeignKey('Driver', related_name='driver', on_delete=models.CASCADE, null=True)

    transport = models.ForeignKey('Transport', on_delete=models.CASCADE, null=True)

    client = models.ForeignKey('Client', on_delete=models.CASCADE, null=True)

    cargo = models.ForeignKey('Cargo', on_delete=models.CASCADE, null=True)

    service = models.ForeignKey('CompanyService', on_delete=models.CASCADE, null=True)

    cost = models.DecimalField(default=0, decimal_places=2, max_digits=30)

    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['date', 'cost']

    def __str__(self):
        return f'{self.date} driver: {self.driver} client: {self.client}'


class ServiceCategory(models.Model):
    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return f'{self.name}'


class CompanyService(models.Model):
    name = models.CharField(max_length=255, blank=False)

    category = models.ManyToManyField(ServiceCategory)

    cost = models.DecimalField(default=0, decimal_places=2, max_digits=30)

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    name = models.CharField(max_length=255, blank=False)

    short_description = models.CharField(max_length=255, blank=False)

    description = models.CharField(max_length=2550, blank=False)

    image = models.ImageField(upload_to='order/static/images/posts/')

    def __str__(self):
        return f'{self.name}'


class Faq(models.Model):
    question = models.CharField(max_length=255, blank=False)

    date = models.DateField()

    response = models.TextField(blank=False)

    def __str__(self):
        return f'{self.question}'


class Coupon(models.Model):
    name = models.CharField(max_length=255, blank=False)

    number = models.IntegerField(blank=False, null=False)

    discount = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return f'{self.name}'


class Review(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    rating = models.IntegerField()
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

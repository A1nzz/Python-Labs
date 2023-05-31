from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('services', views.services_list, name='services'),
    path('drivers', views.drivers_list, name='drivers'),
    path('transport', views.transport_list, name='transport')
]

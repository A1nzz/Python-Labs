from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^services/$', views.services_list, name='services'),
    re_path(r'^drivers/$', views.drivers_list, name='drivers'),
    re_path(r'^transport/$', views.transport_list, name='transport'),
    re_path(r'^orders/$', views.orders_list, name='orders'),
    re_path(r'^create-order/$', views.create_order),


    path('transport/create/', views.create_transport),
    re_path(r'^create-transport-page/$', views.body_type_list),
    re_path(r'^create-transport-page/$', views.createtransport_page, name='createtransport_page'),
    re_path(r'^create-transport/$', views.create_transport, name='create-transport')
]

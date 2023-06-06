from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),

    re_path(r'^drivers/$', views.drivers_list, name='drivers'),
    re_path(r'^transport/$', views.transport_list, name='transport'),
    re_path(r'^orders/$', views.orders_list, name='orders'),
    re_path(r'^create-order/$', views.create_user_order, name='create_user_order'),

    path('transport/create/', views.create_transport),
    path('transport/edit/<int:id>/', views.edit_transport, name='edit_transport'),
    path('transport/delete/<int:id>/', views.delete_transport, name='delete_transport'),
    re_path(r'^create-transport/$', views.create_transport, name='create-transport'),

    re_path(r'^cargo/$', views.cargos_list, name='cargos_list'),
    re_path(r'^create-cargo/$', views.create_cargo, name='create-cargo'),
    path('cargo/edit/<int:id>/', views.edit_cargo, name='edit_cargo'),
    path('cargo/delete/<int:id>/', views.delete_cargo, name='delete_cargo'),

    path('clients/', views.clients_list, name='clients_list'),
    path('clients/create', views.create_client, name='create-client'),
    path('clients/edit/<int:id>/', views.edit_client, name='edit_client'),
    path('clients/delete/<int:id>/', views.delete_client, name='delete_client'),

    path('services/', views.services_list, name='services'),
    path('services/create', views.create_service, name='create-service'),
    path('services/edit/<int:id>/', views.edit_service, name='edit_service'),
    path('services/delete/<int:id>/', views.delete_service, name='delete_service'),
]

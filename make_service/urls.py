from django.shortcuts import render
from django.urls import path
from make_service import views
from .views import *

urlpatterns = [

    path('', views.service_home, name='service_home'),
    path('select_station/', views.select_station, name='select_station'),
    path('addservicestation/', views.addservicestation, name='addservicestation'),
    path('services/<int:ser_id>', views.services, name='services'),
    path('hide_ser_station/<int:stid3>/', views.hide_ser_station, name="hide_ser_station"),
    path('show_serstation/<int:stid2>/', views.show_serstation, name="show_serstation"),
    path('service_station_list/', views.service_station_list, name='service_station_list'),   
    path('myservice_station/', views.myservice_station, name='myservice_station'),    
    path('add_services/<int:ser_id>', views.add_services, name='add_services'),   
    path('bookservice/', views.bookservice, name='bookservice'),   
    path('worker_dash/', views.worker_dash, name='worker_dash'),
    path('closed_service_station/', views.closed_service_station, name='closed_service_station'),   
    path('attend_service_booking/<int:booking_id>/', views.attend_service_booking, name='attend_service_booking'),
    path('ser_update/<int:stid2>', views.ser_update, name='ser_update'),
    path('ser_delete/<int:stid2>', views.ser_delete, name='ser_delete'),
    path('delete_service/<int:stid2>', views.delete_service, name='delete_service'),
    path('mybooking/', views.mybooking, name='mybooking'),   
    path('delete_my_ser_booked/<int:stid2>', views.delete_my_ser_booked, name='delete_my_ser_booked'),   
    path('ser_station_booked/', views.ser_station_booked, name='ser_station_booked'),   




    
]



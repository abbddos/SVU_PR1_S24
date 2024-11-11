from django.urls import path
from . import views

urlpatterns = [
    path('new_Service/', views.CreateService, name='create_Service'),
    path('GetAllServices/' views.GetAllServices, name='GetAllServices'),
    path('GetServiceByID/<uid>', views.GetServiceByID, name='GetServiceByID'),
    path('UpdateService/<uid>', views.UpdateService, name='UpdateService'),
    path('DeleteService/<uid>', views.DeleteUser, name='DeleteService')
]
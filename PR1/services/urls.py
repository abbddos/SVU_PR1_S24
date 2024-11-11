from django.urls import path
from . import views

urlpatterns = [
    path('new_Service/', views.CreateService, name='create_Service'),
    path('GetAllServices/', views.GetAllServices, name='GetAllServices'),
    path('GetServiceByID/<sid>', views.GetServiceByID, name='GetServiceByID'),
    path('UpdateService/<sid>', views.UpdateService, name='UpdateService'),
    path('DeleteService/<sid>', views.DeleteService, name='DeleteService')
]
from django.urls import path
from . import views

urlpatterns = [
    path('new_activity/', views.CreateActivity, name='create_activity'),
    path('GetAllActivities/' views.GetAllActivities, name='GetAllActivities'),
    path('GetActivityByID/<uid>', views.GetActivityByID, name='GetActivityByID'),
    path('UpdateActivity/<uid>', views.UpdateActivity, name='UpdateActivity'),
    path('DeleteActivity/<uid>', views.DeleteUser, name='DeleteActivity')
]
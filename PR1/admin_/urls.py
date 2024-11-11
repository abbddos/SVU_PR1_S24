from django.urls import path
from . import views

urlpatterns = [
    path('new_user/', views.CreateUser, name='create_user'),
    path('GetAllUsers/' views.GetAllUsers, name='GetAllUsers'),
    path('GetUserByID/<uid>', views.GetUserByID, name='GetUserByID'),
    path('UpdateUser/<uid>', views.UpdateUser, name='UpdateUser'),
    path('DeleteUser/<uid>', views.DeleteUser, name='DeleteUser')
]
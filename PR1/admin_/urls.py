from django.urls import path
from . import views

urlpatterns = [
    path('new_user/', views.CreateUser, name='create_user'),
    path('GetAllUsers/', views.GetAllUsers, name='GetAllUsers'),
    path('GetUserByID/<uid>', views.GetUserByID, name='GetUserByID'),
    path('UpdateUser/<uid>', views.UpdateUser, name='UpdateUser'),
    path('UpdateProfile/<uid>', views.UpdateProfile, name='UpdateProfile'),
    path('DeleteUser/<uid>', views.DeleteUser, name='DeleteUser'),
    path('UserProfile/<uid>', views.UserProfile, name = 'UserProfile'),
    path('ChangePassword/<uid>', views.ChangePassword, name = 'change_password'),
    path('register_user/', views.RegisterUser, name='register_user')
]
from django.urls import path
from . import views

urlpatterns = [
    path('new_activity/', views.CreateActivity, name='create_activity'),
    path('GetAllActivities/', views.GetAllActivities, name='GetAllActivities'),
    path('GetActivityByID/<aid>', views.GetActivityByID, name='GetActivityByID'),
    path('UpdateActivity/<aid>', views.UpdateActivity, name='UpdateActivity'),
    path('DeleteActivity/<aid>', views.DeleteActivity, name='DeleteActivity'),
    path('register_activity/', views.RegisterActivity, name = 'register_activity'),
    path('history/<bid>', views.ViewHistory, name = 'history')
]
from django.urls import path
from . import views

urlpatterns = [
    path('new_Beneficiary/', views.CreateBeneficiary, name='create_Beneficiary'),
    path('GetAllBeneficiaries/', views.GetAllBeneficiaries, name='GetAllBeneficiaries'),
    path('GetBeneficiaryByID/<bid>', views.GetBeneficiaryByID, name='GetBeneficiaryByID'),
    path('UpdateBeneficiary/<bid>', views.UpdateBeneficiary, name='UpdateBeneficiary'),
    path('DeleteBeneficiary/<bid>', views.DeleteBeneficiary, name='DeleteBeneficiary')
]
from django.urls import path
from . import views

urlpatterns = [
    path('beneficiaries_register/', views.Beneficiaries, name='beneficiaries_register'),
    path('new_Beneficiary/', views.CreateBeneficiary, name='create_Beneficiary'),
    path('GetAllBeneficiaries/', views.GetAllBeneficiaries, name='GetAllBeneficiaries'),
    path('GetBeneficiaryByID/<bid>', views.GetBeneficiaryByID, name='GetBeneficiaryByID'),
    path('UpdateBeneficiary/<bid>', views.UpdateBeneficiary, name='UpdateBeneficiary'),
    path('DeleteBeneficiary/<bid>', views.DeleteBeneficiary, name='DeleteBeneficiary'),
    path('PrintID/<bid>', views.PrintID, name = 'print-id')
]
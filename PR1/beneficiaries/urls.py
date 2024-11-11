from django.urls import path
from . import views

urlpatterns = [
    path('new_Beneficiary/', views.CreateBeneficiary, name='create_Beneficiary'),
    path('GetAllBeneficiaries/' views.GetAllBeneficiaries, name='GetAllBeneficiaries'),
    path('GetBeneficiaryByID/<uid>', views.GetBeneficiaryByID, name='GetBeneficiaryByID'),
    path('UpdateBeneficiary/<uid>', views.UpdateBeneficiary, name='UpdateBeneficiary'),
    path('DeleteBeneficiary/<uid>', views.DeleteUser, name='DeleteBeneficiary')
]
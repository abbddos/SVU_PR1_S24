from django.db import models
from services.models import Service 
from beneficiaries.models import Beneficiary 

class Activity(models.Model):
    activity_id = models.IntegerField(primary_key = True)
    service = models.ForeignKey(Service, on_delete = models.CASCADE)
    beneficiary = models.ForeignKey(Beneficiary, on_delete = models.CASCADE)



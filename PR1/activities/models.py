from django.db import models
from services.models import Service 
from beneficiaries.models import Beneficiary 

class Activity(models.Model):

    activity_id = models.AutoField(primary_key = True)
    service = models.ForeignKey(Service, on_delete = models.CASCADE)
    beneficiary = models.ForeignKey(Beneficiary, on_delete = models.CASCADE)
    comments = models.TextField(null = True, blank = True)
    last_updated_by = models.EmailField(max_length=254, null = True, blank = True)





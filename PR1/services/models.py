from django.db import models
import datetime

class Service(models.Model):
    service_id = models.AutoField(primary_key = True)
    service_type = models.CharField(max_length = 50, choices = [
        ('GFA','GFA'),
        ('NFI','NFI'),
        ('WASH','WASH'),
        ('PSS','PSS'),
        ('LEG','LEG'),
        ('LH','LH'),
        ('CD','CD')
    ], null = False, blank = False)

    # Abbreviations: 
    # GFA: General Food Assistance.
    # NFI: Non-Food Items.
    # WASH: WAter, Sanitation and Health.
    # PSS: Psycho-Social Support.
    # LEG: LEGal services.
    # LH:  LiveliHoods
    # CD:  Capacity Development.
    
    service_description = models.TextField(null = True, blank = True)
    
    governorate =  models.CharField(max_length = 50, null = False, blank = False)
    district = models.CharField(max_length = 50, null = False, blank = False)
    sub_district = models.CharField(max_length = 50, null = False, blank = False)
    village_neighborhood = models.CharField(max_length = 50, null = False, blank = False)

    start_date = models.DateField(default = datetime.date.today, null = False, blank = False)
    end_date = models.DateField(null = False, blank = False)
    last_updated_by = models.EmailField(max_length=254, null = True, blank = True) 



    def __str__(self):
        return f'Service: {self.service_id} Type: {self.service_type}'
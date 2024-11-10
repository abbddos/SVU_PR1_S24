from django.db import models

class Beneficiary(models.Model):
    beneficiary_id = models.IntegerField(primary_key = True)
    first_name = models.CharField(max_length = 50, null = False, blank = False)
    middle_name = models.CharField(max_length = 50, null = False, blank = False)
    last_name = models.CharField(max_length = 50, null = False, blank = False)
    date_of_birth = models.DateField(null = False, blank = False)
    place_of_birth = models.CharField(max_length = 100, null = False, blank = False)
    sex = models.CharField(max_length = 10, choices = [('Male','Male'), ('Female','Female')])
    national_identifier_type = models.CharField(max_length = 20, choices = [
        ('National ID','National ID'),
        ('Family Booklet','Family Booklet'),
        ('Other','Other'),
        ('None','None')
    ], default = 'None', null = False, blank = False)

    national_identifier_number = models.CharField(max_length = 100)

    contact_number = models.CharField(max_length=10, null = False, blank = False)
    current_address = models.CharField(max_length=100, null = False, blank = False)
    displacement_status=models.CharField(max_length = 15, choices = [
        ('IDP', 'IDP'),
        ('Refugee','Refugee'),
        ('Returnee','Returnee'),
        ('Resident', 'Resident')
    ], null = False, blank = False)

    householod_size = models.IntegerField(default = 1, null = False, blank = False)
    disability_in_household = models.CharField(max_length = 3, choices = [('Yes','Yes'),('No','No')], default = 'No', null = False, blank = False)
    disability_type = models.CharField(max_length = 25, choices = [
        ('None','None'),
        ('Mobility','Mobility'),
        ('Vision','Vision'),
        ('Hearing','Hearing'),
        ('Mental','Mental')
    ], default = 'None', null = False, blank = False)
    elders_in_household = models.CharField(max_length = 5, choices = [('Yes','Yes'),('No','No')], default = 'No', null = False, blank = False)
    infants_in_household = models.CharField(max_length = 5, choices = [('Yes','Yes'),('No','No')], default = 'No', null = False, blank = False)

    occupation = models.CharField(max_length=100, null=False, blank=False, default = 'None')
    education = models.CharField(max_length=100, choices = [
        ('None','None'),
        ('Primary','Primary'),
        ('Intermediate','Intermediate'),
        ('Secondary','Secondary'),
        ('Collage-University','Collage-University'),
        ('Post Grad','Post Grad')
    ], default = 'None', null = False, blank = False)

    def __str__(self):
        return f'Beneficiary ID: {self.beneficiary_id} Name: {str(self.last_name).upper()}, {self.first_name} {self.middle_name}, Sex: {self.sex}, Status: {self.displacement_status}'

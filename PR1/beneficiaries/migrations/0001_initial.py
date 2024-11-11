# Generated by Django 5.1.2 on 2024-11-10 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beneficiary',
            fields=[
                ('beneficiary_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('place_of_birth', models.CharField(max_length=100)),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('national_identifier_type', models.CharField(choices=[('National ID', 'National ID'), ('Family Booklet', 'Family Booklet'), ('Other', 'Other'), ('None', 'None')], default='None', max_length=20)),
                ('national_identifier_number', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=10)),
                ('current_address', models.CharField(max_length=100)),
                ('displacement_status', models.CharField(choices=[('IDP', 'IDP'), ('Refugee', 'Refugee'), ('Returnee', 'Returnee'), ('Resident', 'Resident')], max_length=15)),
                ('householod_size', models.IntegerField(default=1)),
                ('disability_in_household', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=3)),
                ('disability_type', models.CharField(choices=[('None', 'None'), ('Mobility', 'Mobility'), ('Vision', 'Vision'), ('Hearing', 'Hearing'), ('Mental', 'Mental')], default='None', max_length=25)),
                ('elders_in_household', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=5)),
                ('infants_in_household', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=5)),
            ],
        ),
    ]
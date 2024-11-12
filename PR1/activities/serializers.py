from rest_framework import serializers
from .models import Activity
from services.serializers import ServiceSerializer
from services.models import Service
from beneficiaries.serializers import BeneficiarySerializer
from beneficiaries.models import Beneficiary

class ActivitySerializer(serializers.ModelSerializer):  

    beneficiary = BeneficiarySerializer()
    service = ServiceSerializer()

    class Meta:
        model = Activity
        fields = '__all__'

    def create(self, validated_data):
        beneficiary_data = validated_data.pop('beneficiary')
        service_data = validated_data.pop('service')
        beneficiary, _ = Beneficiary.objects.get_or_create(**beneficiary_data)
        service, _ = Service.objects.get_or_create(**service_data)
        activity = Activity.objects.create(beneficiary = beneficiary, service=service, **validated_data)
        return activity

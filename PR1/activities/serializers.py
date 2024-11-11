from rest_framework import serializers
from beneficiaries.serializers import BeneficiarySerializer
from services.serializers import ServiceSerializer
from .models import Activity

class ActivitySerializer(serializers.ModelSerializer):
#    service = ServiceSerializer()
#    beneficiary = BeneficiarySerializer()
    
    class Meta:
        model = Activity
        fields = '__all__'
#        depth = 1

#    def get_service_detail(self, obj):
#        return ServiceSerializer(obj.service).data 

#    def get_beneficiary_detail(self, obj):
#        return BeneficiarySerializer(obj.beneficiary).data
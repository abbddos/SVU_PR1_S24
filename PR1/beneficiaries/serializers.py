from rest_framework import serializers
from .models import Beneficiary

class BeneficiarySerializer(serializers.ModelSerializer):

    beneficiary_id = serializers.IntegerField(required=False)
    class Meta:
        model = Beneficiary
        fields = '__all__'
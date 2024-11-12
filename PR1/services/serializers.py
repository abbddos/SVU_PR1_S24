from rest_framework import serializers
from .models import Service

class ServiceSerializer(serializers.ModelSerializer):
    
    service_id = serializers.IntegerField(required=False)
    class Meta:
        model = Service
        fields = '__all__'
from .models import mission
from rest_framework import serializers


class missionSerializer(serializers.ModelSerializer):
    class Meta:
        model = mission
        fields = '__all__'
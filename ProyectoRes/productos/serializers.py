from rest_framework import serializers
from .models import Jugo

class JugoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jugo
        fields = '__all__'

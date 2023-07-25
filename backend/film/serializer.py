
from rest_framework import serializers
from .models import Film

class FilmsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Film
        fields= '__all__'
        depth= 1
        
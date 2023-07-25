
from rest_framework import serializers
from acteur.serializer import ActorsSerializer
from .models import Film

class FilmsSerializer(serializers.ModelSerializer):
    actors = ActorsSerializer(many=True)
    class Meta:
        model= Film
        fields= '__all__'
        
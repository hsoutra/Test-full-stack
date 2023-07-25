
from rest_framework import serializers
from acteur.serializer import ActorsSerializer
from review.serializer import ReviewSerializer
from .models import Film

class FilmsSerializer(serializers.ModelSerializer):
    actors = ActorsSerializer(many=True)
    reviews = ReviewSerializer(many=True)
    class Meta:
        model= Film
        fields= '__all__'
        
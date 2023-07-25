
from rest_framework import serializers
from .models import Actor

class ActorsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Actor
        fields= '__all__'
        unique_together = [
            ("first_name", "last_name"),
        ]
        
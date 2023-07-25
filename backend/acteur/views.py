from .models import Actor
from rest_framework import viewsets
from .serializer import ActorsSerializer

class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorsSerializer
 
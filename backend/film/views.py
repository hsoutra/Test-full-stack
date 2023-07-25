from film.models import Film
from rest_framework import viewsets
from film.serializer import FilmsSerializer
# Create your views here.
class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmsSerializer
 
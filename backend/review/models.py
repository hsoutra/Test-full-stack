from django.db import models
from film.models import Film
from .validation import validate_grade

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    grade= models.PositiveIntegerField(null=False, validators=[validate_grade])
    film = models.ForeignKey(Film, related_name="reviews", on_delete= models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)
    
    
    
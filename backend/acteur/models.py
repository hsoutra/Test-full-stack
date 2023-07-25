from django.db import models

from film.models import Film

class Actor(models.Model):
    id = models.AutoField(primary_key=True)
    first_name= models.CharField(max_length=256, null=False)
    last_name= models.CharField(max_length=256, null=False)
    film = models.ForeignKey(Film, related_name="actors", on_delete= models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)
    class Meta:
        unique_together = [
            ("first_name", "last_name"),
        ]
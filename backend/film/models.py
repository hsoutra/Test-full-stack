from django.db import models

class Film(models.Model):
    id = models.AutoField(primary_key=True)
    titre= models.CharField(max_length=256, null=False)
    description= models.TextField(null=True)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)

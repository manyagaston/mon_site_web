
from django.db import models


class home(models.Model):
    nom = models.CharField(max_length=255)
    
    
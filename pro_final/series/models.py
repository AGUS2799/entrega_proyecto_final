from django.db import models

# Create your models here.
class Series(models.Model):
    name = models.CharField(max_length=40)
    release_date = models.DateField()
    director_name = models.CharField(max_length=40)
    description = models.TextField(blank= True, null=True)


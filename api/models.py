from django.db import models

# Create your models here.


class Favourites(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    height = models.IntegerField()
    weight = models.IntegerField()
    order = models.IntegerField()
    icon = models.CharField(max_length=500)
    abilities = models.IntegerField()
    forms = models.IntegerField()
    types = models.IntegerField()

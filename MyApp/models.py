from django.db import models

class HouseData(models.Model):
    Area = models.CharField(max_length=50) 
    Price = models.IntegerField()
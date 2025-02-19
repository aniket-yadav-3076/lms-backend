from django.db import models

class learn(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    discount = models.IntegerField()
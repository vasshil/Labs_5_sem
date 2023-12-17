from django.db import models


class Token(models.Model):
    value = models.CharField(max_length=36, unique=True)


class Good(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    price = models.IntegerField()


from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=120)
    price = models.FloatField()
    available_amount = models.IntegerField()
    author = models.ForeignKey("Author", on_delete=models.CASCADE)


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

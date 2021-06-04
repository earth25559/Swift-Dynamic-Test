from django.db import models
from django.forms import widgets

# Create your models here.


class Customer(models.Model):
    email = models.EmailField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Create your models here.

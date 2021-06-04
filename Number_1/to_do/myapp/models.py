from django.db import models
from django.forms import widgets

# Create your models here.


class Tasks(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateTimeField(
        auto_now_add=False, auto_now=False, blank=True, null=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

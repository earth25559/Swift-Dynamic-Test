from django import forms
from django.forms import ModelForm

from .models import *


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['email', 'name']

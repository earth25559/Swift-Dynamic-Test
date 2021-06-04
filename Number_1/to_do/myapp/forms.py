from django import forms
from django.forms import ModelForm

from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class TaskForm(forms.ModelForm):
    due_date = forms.DateField(widget=DateInput)

    class Meta:
        model = Tasks
        fields = ['title', 'due_date']


class UpdateForm(forms.ModelForm):
    due_date = forms.DateField(widget=DateInput)

    class Meta:
        model = Tasks
        fields = ['title', 'due_date', 'complete']

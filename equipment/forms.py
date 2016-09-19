# coding: utf-8

from django.forms import ModelForm
from .models import Application
from django import forms

class  ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ('name', 'organization', 'email', 'phone', 
                  'content', 'equipment', 'starttime', 'endtime')

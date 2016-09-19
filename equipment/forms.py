# coding: utf-8

from django.forms import ModelForm
from .models import Application
from django import forms


class  ApplicationForm(ModelForm):

    class Meta:
        model = ScheduleModel
        fields = ('name', 'organization', 'email','num')

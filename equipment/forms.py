# coding: utf-8

from django.forms import ModelForm
from .models import Application
from django import forms
from django.utils.translation import gettext as _

class  ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ('name', 'organization', 'email', 'phone', 
                  'content', 'equipment', 'starttime', 'endtime'
                  )
    
#     def clean_starttime(self):
#         data = self.cleaned_data['starttime']
#         equipment = self.cleaned_data['equipment']
#         if Application.objects.filter(starttime__gte=data,
#                                       endtime__lte=data,
#                                       status='3',
#                                       equipment=equipment
#                                       ).exists():
#             raise forms.ValidationError(_("Данное время уже занято"))
#         return data

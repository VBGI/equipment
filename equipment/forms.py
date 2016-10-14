# coding: utf-8

from django.forms import ModelForm
from .models import Application
from django import forms
from django.utils.translation import gettext as _
from django.utils import timezone



class  ApplicationForm(ModelForm):
    required_css_class = 'required'
        
    class Meta:
        model = Application
        fields = ('name', 'organization', 'email', 'phone', 
                  'content', 'equipment', 'startdate', 'enddate'
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

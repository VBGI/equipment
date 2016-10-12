from django.conf.urls import *
from equipment.views import request_rent

urlpatterns = patterns('',
   url(r'^', request_rent, name="equipment-app")
)
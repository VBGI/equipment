#coding: utf-8
from django.contrib import admin
# from django.utils import timezone
# from django.utils.translation import gettext as _
from .models import Equipment, Application


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization', 'startdate', 'enddate')
    list_filter = ('status', 'equipment', 'startdate', 'enddate', 'created')
    readonly_fields = ('unum',)

class EquipmentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Application, ApplicationAdmin)

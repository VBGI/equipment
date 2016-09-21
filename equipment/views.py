import gc

from django.http import HttpResponse
from django.template import RequestContext
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.utils.translation import gettext as _
from django.template.loader import render_to_string

from .forms import ApplicationForm

from .models import Application, Equipment
from .messages import *


@never_cache
@csrf_protect
def request_rent(request):
    response_data = {'error' : ''}

    if request.method == 'GET':
        unum = request.GET.get('unum', '')
        pk = request.GET.get('pk', '')
        obj = Application.objects.filter(unum=unum, id=pk)
        if obj.exists():
            send_mail(app_created_theme.format(obj[0].created),
                      app_deleted % (obj[0].name, obj[0].equipment,
                                     obj[0].startdate, obj[0].enddate),
                      'equipment@botsad.ru', [cmail], fail_silently=True)
            obj[0].delete()
            return HttpResponse('<h2>{}</h2>'.format(app_del_completed))
        
    if request.method == 'POST':
        form = ApplicationForm(request)
        if form.is_valid():
            name = form.cleaned_data['name']
            org = form.cleaned_data['organization']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            content = form.cleaned_data['content']
            equipment = form.cleaned_data['equipment']
            starttime = form.cleaned_data['starttime'] 
            endtime = form.cleaned_data['endtime'] 
            try:
                equip = Equipment.objects.get(pk=equipment)
                application = Application.objects.create(name=name,
                                      organization=org,
                                      email=email,
                                      phone=phone,
                                      content=content,
                                      starttime=starttime,
                                      endtime=endtime,
                                      equipment=equip
                                      )
                send_mail(app_created_theme.format(application.created),
                          app_created % (uname, application.equipment,
                                         application.starttime,
                                         application.endtime,
                                         # TODO: Remove url by hash needed
                                         ),
                          'equipment@botsad.ru', [application.email], fail_silently=True)
            except Equipment.DoesNotExists:
                response_data.update({'error': _('Такого оборудования нет')})
            response_data.update({'form' : form})
        
        result = render_to_string('equipment_form.html', context,  context_instance=RequestContext(request))
        gc.collect()
        return HttpResponse(result, content_type='text/plain')
            

# 


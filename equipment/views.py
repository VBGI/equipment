import json

from django.http import HttpResponse
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.core.mail import send_mail
from django.core.urlresolvers import reverse

from .forms import ApplicationForm

from .models import Application
from .messages import *

import re



@never_cache
@csrf_protect
def register_user(request):
    response_data = {'error' : '', 'msg': ''}
    
    if request.method == 'GET':
        unum = request.GET.get('unum', '')
        pk = request.GET.get('pk', '')
        obj = Application.objects.filter(unum=unum, id=pk)
        if obj.exists():
            send_mail(app_created_theme.format(), # TODO: needs to be updated 
                      app_deleted % (obj[0].name, obj[0].equipment,
                                     obj[0].startdate, obj[0].enddate),
                      'equipment@botsad.ru', [cmail], fail_silently=True)
            obj[0].delete()
            return HttpResponse('<h2>{}</h2>'.format(app_del_completed))
        
#     if request.method == 'POST':
#         timepk = request.POST.get('timepk', None)
#         uname = request.POST.get('username', '')
#         uphone = request.POST.get('phone', '') 
#         umail = request.POST.get('email', '') 
#         unum = request.POST.get('num', '')        
#         err_msg = validate(uname, uphone)
#         if not err_msg:
#             try:
#                 timeobj = ScheduleTimes.objects.get(id=timepk)
#             except ScheduleTimes.DoesNotExist:
#                 response_data.update({'error': 'Неправильно выбрано время'})
#                 return HttpResponse(json.dumps(response_data), content_type="application/json")
#             if timeobj.get_free_places <= 0:
#                 response_data.update({'error': 'Выбранное время занято'})
#                 return HttpResponse(json.dumps(response_data), content_type="application/json")
#             try:
#                 unum = int(unum)
#                 umod = ScheduleModel.objects.create(username=uname,
#                                                     phone=uphone,
#                                                     email=umail,
#                                                     num=unum,
#                                                     time=timeobj)
#                 hashurl = 'http://botsad.ru' + reverse('bgi-scheduler') + '?hashid=' + umod.hashid
#                 send_mail(u'Регистрация на маршрут "Наука в путешествии. ПриМорье." (Ботанический сад, Владивосток)',
#                           rec_created%(uname, str(umod.time.date.date), str(umod.time.time), hashurl),
#                           'ecocenter@botsad.ru', [umod.email, 'ecocenter@botsad.ru'], fail_silently=True)
#                 response_data.update({'msg': 'Вы успешно зарегистрировались'})
#             except:
#                 response_data.update({'error': 'Что-то пошло не так при регистрации'})
#         else:
#             response_data.update({'error':err_msg})
#     else:
#         response_data['error'] = 'Неправильный запрос'
# 
#     return HttpResponse(json.dumps(response_data), content_type="application/json")
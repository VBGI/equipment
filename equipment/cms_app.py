# -*- coding: utf-8 -*-

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class EquipmentApphook(CMSApp):
    name = _(u"Ajax-служба для бронирования оборудования коллективного пользования")
    urls = ["equipment.urls"]

apphook_pool.register(EquipmentApphook)
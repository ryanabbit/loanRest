# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(RequestHeader)
admin.site.register(Business)
admin.site.register(SelfReportedCashFlow)
admin.site.register(CFApplicationData)
admin.site.register(Owners)
admin.site.register(Address)
admin.site.register(AppStatus)



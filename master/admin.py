#!/usr/bin/env python
#
#       admin.py
#       
#       Copyright 2009 Yousuf Fauzan <yousuffauzan@gmail.com>
#       

from django.contrib import admin
from master.models import *

admin.site.register(Quote)
admin.site.register(Reference)
admin.site.register(EmailCode)
admin.site.register(Tag)
admin.site.register(QuoteBin)

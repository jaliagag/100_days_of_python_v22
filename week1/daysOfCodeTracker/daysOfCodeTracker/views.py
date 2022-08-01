#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse

def hi(request):
    return HttpResponse('hola desde django!')

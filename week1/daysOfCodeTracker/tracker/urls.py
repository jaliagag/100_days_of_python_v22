#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.urls import path

from tracker import views

urlpatterns = [
    path('', views.home1),
    path('home/', views.demo),
]

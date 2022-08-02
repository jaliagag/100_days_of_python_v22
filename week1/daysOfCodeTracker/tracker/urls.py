#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.urls import path

from tracker import views
from django.contrib.auth.views import LogoutView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    path('commits/search/', views.search_commits, name='search_commits'),
    path('search/commits/', views.search_commits_action),
    path('commits/rm/<pk>', views.Delete_commit.as_view(), name='delete_commit'),
    path('commits/<pk>', views.Detail_commit.as_view(), name='detail_commit'),
    path('commits/edit/<pk>', views.Update_commit.as_view(), name='update_commit'),
#    path('commits/add/', views.Create_commit, name='create_commit'),
#    path('commits/list/', views.View_commits, name='list_commits'),
]


# -*- coding: utf-8 -*-
from django.conf.urls import *
from views import *
from django.contrib import admin
from django.core.context_processors import csrf
from django.views.decorators.csrf import ensure_csrf_cookie

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',IndexView.as_view(), {}, name='index'),
    url(r'^newmission/$',NewmissionView.as_view(), {}, name='newmission'),
    url(r'^mission/(?P<pk>\d+)/$',MissionView.as_view(), {}, name='mission'),
)
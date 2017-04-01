from django.conf.urls import url, include
from django.contrib import admin
from .views import (
		index,
		input_med,
		display,
	)

urlpatterns = [
		url(r'^$',index, name='index'),
		url(r'^create/$',input_med),
		url(r'^display/$', display),
]

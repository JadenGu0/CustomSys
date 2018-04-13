from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'commission.views.new', name='index'),
    url(r'^calculate$', 'commission.views.calculate', name='calculate'),
]
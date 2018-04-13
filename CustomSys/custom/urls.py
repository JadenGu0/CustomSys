from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'custom.views.index', name='index'),
    url(r'update$', 'custom.views.update', name='update'),
]
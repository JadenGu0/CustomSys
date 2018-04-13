from django.conf.urls import include, url
from django.contrib import admin
from views import show_login
urlpatterns = [
    # Examples:
    # url(r'^$', 'CustomSys.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'CustomSys.views.show_login', name='show_login'),
    url(r'^login$', 'CustomSys.views.my_login', name='login'),
    url(r'^custom/', include('custom.urls')),
    url(r'^commission/', include('commission.urls')),
]

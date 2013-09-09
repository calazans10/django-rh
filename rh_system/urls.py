from django.conf.urls import patterns, include, url
from django.contrib import admin
from ajax_select import urls as ajax_select_urls


admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rh_system.views.home', name='home'),
    # url(r'^rh_system/', include('rh_system.foo.urls')),

    url(r'^admin/lookups/', include(ajax_select_urls)),
    url(r'^admin/', include(admin.site.urls)),
)

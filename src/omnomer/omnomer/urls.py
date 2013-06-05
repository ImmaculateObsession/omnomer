from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from items import urls as item_urls
from shelves import urls as shelf_urls
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'omnomer.views.home', name='home'),
    # url(r'^omnomer/', include('omnomer.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'omnomer.views.home', name='home'),
    url(r'^items/', include(item_urls)),
    url(r'^shelves/', include(shelf_urls)),
)

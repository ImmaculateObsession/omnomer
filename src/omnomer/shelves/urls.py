from django.conf.urls import patterns, include, url

from shelves.views import *

urlpatterns = patterns('',
    url(r'^list/', ListShelfView.as_view(), name='shelf-list'),
    url(r'^create/', CreateShelfView.as_view(), name='shelf-create'),
    url(r'^edit/(?P<pk>\d+)/$', EditShelfView.as_view(), name='shelf-edit'),
    url(r'^delete/(?P<pk>\d+)/$', DeleteShelfView.as_view(), name='shelf-delete'),
    url(r'^detail/(?P<pk>\d+)/$', DetailShelfView.as_view(), name='shelf-detail')
)
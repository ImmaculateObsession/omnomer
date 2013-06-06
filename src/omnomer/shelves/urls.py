from django.conf.urls import patterns, include, url

from shelves.views import (
    ListShelfView,
    CreateShelfView,
    EditShelfView,
    DeleteShelfView,
    )

urlpatterns = patterns('',
    url(r'^$', ListShelfView.as_view(), name='shelves-list'),
    url(r'^list/', ListShelfView.as_view(), name='shelves-list'),
    url(r'^create/', CreateShelfView.as_view(), name='shelf-create'),
    url(r'^edit/(?P<pk>\d+)/$', EditShelfView.as_view(), name='shelf-edit'),
    url(r'^delete/(?P<pk>\d+)/$', DeleteShelfView.as_view(), name='shelf-delete')
)
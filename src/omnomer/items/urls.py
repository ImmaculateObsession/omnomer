from django.conf.urls import patterns, include, url

from items.views import (
    ListItemView,
    CreateItemView,
    EditItemView,
    DeleteItemView,
)

urlpatterns = patterns('',
    url(r'^list/', ListItemView.as_view(), name='items-list'),
    url(r'^create/', CreateItemView.as_view(), name='item-create'),
    url(r'^edit/(?P<pk>\d+)/$', EditItemView.as_view(), name='item-edit'),
    url(r'^delete/(?P<pk>\d+)/$', DeleteItemView.as_view(), name='item-delete')
)
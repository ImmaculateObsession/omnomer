from django.conf.urls import patterns, include, url

from items.views import (
    ListItemView,
    CreateItemView,
    )

urlpatterns = patterns('',
    url(r'^list/', ListItemView.as_view(), name='items-list'),
    url(r'^create/', CreateItemView.as_view(), name='item-create'),
)
import factory
from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import RequestFactory
from items.models import Item
from items.views import (
    ListItemView,
    CreateItemView,
    EditItemView,
    DeleteItemView,
)

class ItemFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = Item
    FACTORY_DJANGO_GET_OR_CREATE = ('name', 'value', ) #'owners')

    name = factory.Sequence(lambda n: 'test_item{0}'.format(n))
    value = factory.Sequence(lambda n: '{0}'.format(n))
    #owners = factory.SubFactory(UserFactory)

class ItemListViewTests(TestCase):

    def test_items_in_the_context_request_factory(self):

        factory = RequestFactory()
        request = factory.get('/items/list/')

        response = ListItemView.as_view()(request)
        self.assertEquals(list(response.context_data['object_list']), [])

        ItemFactory()
        
        response = ListItemView.as_view()(request)
        self.assertEquals(response.context_data['object_list'].count(), 1)

class ItemCreateViewTests(TestCase):

    def test_items_in_the_context_request_factory(self):

        factory = RequestFactory()
        request = factory.get('/items/')

        response = CreateItemView.as_view()(request)

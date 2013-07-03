from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from model_utils.models import TimeStampedModel
from items.models import Item

class Shelf(TimeStampedModel):

    owners = models.ManyToManyField(User)
    name = models.CharField(max_length=140)
    items = models.ManyToManyField(Item)

    def __str__(self):
        return self.name

    def get_absolute_url(self):

        return reverse('shelf-detail', kwargs={'pk': self.id })

    def __getattribute__(self, name):
        if name == "items" or name == "owners":
            return models.manager.Manager.__getattribute__(self, name).all()
        else:
            return models.manager.Manager.__getattribute__(self, name)

    #TODO:
    # pictures

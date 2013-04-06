from django.db import models
from django.contrib.auth.models import User

from model_utils.models import TimeStampedModel

class Item(TimeStampedModel):

    owners = models.ManyToManyField(User)
    name = models.CharField(max_length=140)
    value = models.DecimalField(max_digits=9, decimal_places=2)
    purchase_date = models.DateTimeField()


    #TODO:
    # barcode
    # location (geotag?) (overriden by shelf?)
    # value
    # purchase date
    # location of purchase
    # extra_fields -> tags
    # user currently in possesion of == owners unless specified
    # pictures




# class eBook(Item):

#   # author
#   # pub date

# class Book(eBook):
#   # isbn10
#   # isbn13

# class ExtraField():
#   # id 
#   # users
#   # items
#   # name
#   # value

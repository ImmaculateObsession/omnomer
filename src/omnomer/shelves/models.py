from django.db import models
from django.contrib.auth.models import User

from model_utils.models import TimeStampedModel
from items.models import Item

class Shelf(TimeStampedModel):

	owners = models.ManyToManyField(User)
	name = models.CharField(max_length=140)
	items = models.ManyToManyField(Item)
	#TODO:
	# id
	# owners
	# items
	# name
	# pictures



from django.db import models

from model_utils import TimeStampedModel

class Item(TimeStampedModel):

	#TODO:
	# id
	# name
	# barcode
	# users it belongs to (many-to-many)
	# location (geotag?) (overriden by shelf?)
	# value
	# purchase date
	# location of purchase
	# extra_fields -> tags
	# user currently in possesion of == owners unless specified
	# pictures




# class eBook(Item):

# 	# author
# 	# pub date

# class Book(eBook):
# 	# isbn10
# 	# isbn13

# class ExtraField():
# 	# id 
# 	# users
# 	# items
# 	# name
# 	# value

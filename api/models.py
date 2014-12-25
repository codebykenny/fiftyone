from django.db import models
from django.utils import timezone

# Create your models here.

class Blog(models.Model):
	category = models.CharField(max_length=30)

	def __str__(self):
		return self.category

class BlogPost(models.Model):
	blog		= models.ForeignKey(Blog)
	title		= models.CharField(max_length=50)
	blurb		= models.CharField(max_length=100)
	image_url	= models.CharField(max_length=200)
	body		= models.CharField(max_length=5000)
	created		= models.DateField(default=timezone.now)
	modified	= models.DateField(default=timezone.now)

	def __str__(self):
		return self.title
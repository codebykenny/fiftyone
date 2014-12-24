from django.db import models

# Create your models here.

class Blog(models.Model):
	category = models.CharField(max_length=30)

	def __str__(self):
		return self.category

class BlogPost(models.Model):
	blog = models.ForeignKey(Blog)
	title = models.CharField(max_length=50)
	blurb = models.CharField(max_length=100)
	body = models.CharField(max_length=5000)

	def __str__(self):
		return self.title
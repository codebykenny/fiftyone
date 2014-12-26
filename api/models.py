from django.db import models
from django.utils import timezone

# Create your models here.

class MyManager(models.Manager):
    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except BlogPost.DoesNotExist:
            return None

class AuthorManager(models.Manager):
	def get_by_natural_key(self, name, profile_image_url):
		return self.get(name=name, profile_image_url=profile_image_url)

class Author(models.Model):
	objects				= AuthorManager()

	name				= models.CharField(max_length=100, unique=True)
	profile_image_url	= models.CharField(max_length=200, unique=True)

	def natural_key(self):
		return (self.name, self.profile_image_url)

	def __str__(self):
		return self.name

class Blog(models.Model):
	category = models.CharField(max_length=30)

	def __str__(self):
		return self.category

class BlogPost(models.Model):
	blog		= models.ForeignKey(Blog)
	author		= models.ForeignKey(Author, null=True, blank=True)
	title		= models.CharField(max_length=50)
	blurb		= models.CharField(max_length=100)
	image_url	= models.CharField(max_length=200)
	body		= models.CharField(max_length=5000)
	created		= models.DateField(default=timezone.now)
	modified	= models.DateField(default=timezone.now)

	objects = MyManager()

	def __str__(self):
		return self.title

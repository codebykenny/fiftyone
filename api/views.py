import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template import RequestContext, loader
from django.core import serializers

from api.models import Blog, BlogPost, Author

# Create your views here.

def latest(request):
	post = BlogPost.objects.all().order_by('created').select_related() [:6]

	post_json = serializers.serialize('json', post)

	return HttpResponse(post_json, content_type="application/json")

def post(request, post_id):
	post = BlogPost.objects.filter(id=post_id)

	post_json = serializers.serialize('json', post, use_natural_primary_keys=True, use_natural_foreign_keys=True)

	if post != None:
		return HttpResponse(post_json, content_type="application/json")
	else:
		return HttpResponseNotFound('<h1>Page not found</h1>')

def category(request, type=None):
	category = BlogPost.objects.filter(blog__category=type.title())

	post_json = serializers.serialize('json', category, use_natural_primary_keys=True, use_natural_foreign_keys=True)

	if type != None:
		return HttpResponse(post_json, content_type="application/json")
	else:
		return HttpResponseNotFound('<h1>Page not found</h1>')
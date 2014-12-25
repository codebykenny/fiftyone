import json
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.core import serializers

from api.models import Blog, BlogPost

# Create your views here.

def latest(request):
	post = BlogPost.objects.all().order_by('created')[:6]

	post_json = serializers.serialize('json', post)

	return HttpResponse(post_json, content_type="application/json")
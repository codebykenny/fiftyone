from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.

def index(request, controller = None, action = None):
	if (controller):
		template = loader.get_template('views/' + controller + '/' + action + '.html')
		context		= RequestContext(request, {})
	else :
		template	= loader.get_template('Home/index.html')
		context		= RequestContext(request, {})


	return HttpResponse(template.render(context))
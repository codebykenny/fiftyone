from django.conf.urls import patterns, url

from api import views

urlpatterns = patterns('',
    # url(r'^$', views.index, name='index'),
    url(r'^latest/$', views.latest, name='latest'),
    url(r'^post/(?P<post_id>\d+)$', views.post, name='post'),
    url(r'^category/(?P<type>\w+)$', views.category, name='category'),
)
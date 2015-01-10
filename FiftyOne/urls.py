from django.conf.urls import patterns, include, url
from django.contrib import admin

from Home import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'FiftyOne.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('Home.urls')),
    url(r'api/', include('api.urls')),
    url(r'^views/(?P<controller>[-_\w]+/$)', views.index, name='index' ),
    url(r'^views/(?P<controller>\w+)/(?P<action>\w+)/$', views.index),
    url(r'^blog/', views.index),
)

from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^forum/', include('forum.urls')),
	url(r'', include('forum.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

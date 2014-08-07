from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required as LR
from forum.models import *
from forum import views 

urlpatterns = patterns('',

	url(r'^index/$', views.index, name="index"),
	url(r'^signUp/$', views.signUp, name="signUp"),
	url(r'^login/$', 'django.contrib.auth.views.login', name="login"),
	url(r'^forumHome/$', views.forumHome, name="forumHome"),
	url(r'^forumView/(?P<forum_id>\d+)/$', views.forumView, name="forumView"),
	url(r'^threadView/(?P<thread_id>\d+)/$', views.threadView, name="threadView"),
	url(r'^startThread/$', views.startThread, name="startThread"),
	url(r'^editProfile/(?P<user_id>\d+)/$', views.editProfile, name="editProfile"),
		)	

from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required as LR
from forum.models import *
from forum import views 

urlpatterns = patterns('',

	url(r'^Index/$', views.Index, name="index"),
	url(r'^ForumHome/$', views.ForumHome, name="ForumHome"),
	url(r'^ForumView/(?P<forum_id>\d+)/$', views.ForumView, name="ForumView"),
	url(r'^ThreadView/(?P<thread_id>\d+)/$', views.ThreadView, name="ThreadView"),
	url(r'^EditProfile/(?P<user_id>\d+)/$', views.EditProfile, name="EditProfile"),
	)	

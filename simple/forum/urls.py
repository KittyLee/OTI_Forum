from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required as LR
from forum.models import *
from forum import views 

urlpatterns = patterns('',

	url(r'^Forum/$', views.Main, name="Main"),
	url(r'^ForumView/(?P<Forum_title>\d+)/$', views.ForumView, name="ForumView"),
	url(r'^ThreadView/(?P<Thread_title>\d+)/$', views.ThreadView, name="ThreadView"),
	url(r'^EditProfile/(?P<UserProfile_user>\d+)/$', views.EditProfile, name="EditProfile"),
	)	
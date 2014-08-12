from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required as LR
from forum.models import *
from forum import views 

urlpatterns = patterns('',

	url(r'^index/$', views.index, name="index"),
	url(r'^signUp/$', views.signUp, name="signUp"),
	url(r'^login/$', 'django.contrib.auth.views.login', name="login"),
	url(r'^logout/$', 'django.contrib.auth.views.logout', name="logout"),
	url(r'^forumHome/$', views.forumHome, name="forumHome"),
	url(r'^newForum/$', views.newForum, name="newForum"),
	url(r'^newThread/(?P<forum_id>\d+)/$', views.newThread, name="newThread"),
	url(r'^forumView/(?P<forum_id>\d+)/$', views.forumView, name="forumView"),
	url(r'^threadView/(?P<thread_id>\d+)/$', views.threadView, name="threadView"),
	url(r'^reply/(?P<thread_id>\d+)/$', views.reply, name="reply"),
	url(r'^editProfile/$', views.editProfile, name="editProfile"),
	url(r'^accounts/profile/$', views.userProfile, name="userProfile"),
	url(r'^userProfile/(?P<user_id>\d+)/$', views.userProfile, name="userProfile"),
	url(r'^documents/$', views.documents, name="documents"),
		)	

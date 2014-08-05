import urlparse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from forum.models import Forum, Thread, Post, UserProfile
from django.core.urlresolvers import reverse


from django.template.loader import get_template
# Create your views here.

def index(request):
	return render(request, "Index.html",)

def forumHome(request):
	all_forums = Forum.objects.all()
	return render(request, 'Forums.html', {'all_forums': all_forums})

def forumView(request,forum_id):
	forum = get_object_or_404(Forum, pk=forum_id)
	all_threads = Thread.objects.filter(forum=forum).all()
	return render(request, 'ForumView.html', {'forum': forum, 'all_threads': all_threads})

def threadView(request,thread_id):
	thread = get_object_or_404(Thread, pk=thread_id)
	all_posts = Post.objects.filter(thread=thread).all()
	return render(request, 'ThreadView.html', {'thread': thread, 'all_posts': all_posts})

def editProfile(request,user_id):
	profile = get_object_or_404(UserProfile, pk=user_id)
	return render(request, 'profile.html', {'profile': profile})

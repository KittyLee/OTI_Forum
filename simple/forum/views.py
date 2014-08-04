from django.shortcuts import render, get_object_or_404
from forum.models import Forum, Thread, Post, UserProfile

from django.template.loader import get_template
# Create your views here.

def Index(request):
	return render(request, "Index.html",)

def ForumHome(request):
	all_forums = Forum.objects.all()
	return render(request, 'Forums.html', {'all_forums': all_forums})

def ForumView(request, forum_id):
	forum = get_object_or_404(Forum, pk= forum_id)
	all_threads = Thread.objects.filter( forum = forum).all()
	return render(request, 'ForumView.html', {'forum': forum, 'all_threads': all_threads})

def ThreadView(request, thread_id):
	threadview = get_object_or_404(thread, pk=thread_id)
	return render(request, 'Thread.html', {'threadview': threadview})

def EditProfile(request, user_id):
	UserProfile = get_object_or_404(UserProfile, pk=user_id)
	return render(request, 'profile.html', {'editprofile': editprofile})

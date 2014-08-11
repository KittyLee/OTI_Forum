import urlparse
from forms import ProfileForm, PostForm, ForumForm, ThreadForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from forum.models import Forum, Thread, Post, UserProfile
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from django.template.loader import get_template

# Create your views here.
def login(request):
	username =request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
	return HttpResponseRedirect("/userProfile/%s/" % request.user.id)

def logout(request):
	logout(request)

def signUp(request):
	modelform = ProfileForm()
	if request.method == 'POST':
		modelform = ProfileForm(request.POST)
	if modelform.is_valid():
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		# We'll do the password check in a second
		u = User.objects.create_user(first_name = first_name, last_name = last_name, email = email, password = password, username=username)	
		u.save()
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				
		return HttpResponseRedirect("/editProfile/%s/" % request.user.id)
	return render(request, 'signUp.html', {'modelform': modelform})

def index(request):
	return render(request, "index.html",)

def forumHome(request):
	all_forums = Forum.objects.all()
	return render(request, 'forums.html', {'all_forums': all_forums})

def newForum(request):
	modelform = ForumForm()
	if request.method == 'POST':
		modelform = ForumForm(request.POST)
	if modelform.is_valid():
		title = modelform.cleaned_data['title']
		newforum = Forum(title = title)
		newforum.save()
		return HttpResponseRedirect("/forum/forumHome/")
	return render(request, 'newForum.html', {'modelform': modelform})

def forumView(request,forum_id):
	forum = get_object_or_404(Forum, pk=forum_id)
	all_threads = Thread.objects.filter(forum=forum).all()
	return render(request, 'forumView.html', {'forum': forum, 'all_threads': all_threads})

def threadView(request,thread_id):
	thread = get_object_or_404(Thread, pk=thread_id)
	all_posts = Post.objects.filter(thread=thread).all()
	return render(request, 'threadView.html', {'thread': thread, 'all_posts': all_posts})

def newThread(request, forum_id):
	modelform = ThreadForm()
	if request.method == 'POST':
		modelform = ThreadForm(request.POST)
	if modelform.is_valid():
		title = modelform.cleaned_data['title']
		forum = get_object_or_404(Forum, pk=forum_id)
		newthread = Thread(title = title, forum = forum)
		newthread.save()
		return HttpResponseRedirect("/forum/forumView/%s/" % forum_id)
	return render(request, 'newThread.html', {'modelform': modelform})

def reply(request, thread_id):
	modelform = PostForm()
	if request.method == 'POST':
		modelform = PostForm(request.POST)
	if modelform.is_valid():
		title = modelform.cleaned_data['title']
		body = modelform.cleaned_data['body']
		thread = get_object_or_404(Thread, pk=thread_id)
		newpost = Post(title = title, body = body, creator = request.user, thread = thread )
		newpost.save()
		return HttpResponseRedirect("/forum/threadView/%s/" % thread_id)
	return render(request, 'reply.html', {'modelform': modelform})


def editProfile(request,user_id):
	profile = get_object_or_404(UserProfile, pk=user_id)
	return render(request, 'profile.html', {'profile': profile})

def userProfile(request,user_id):
	profile = UserProfile.objects.get_or_create(user = user)[0]
	return render(request, 'userProfile.html', kwargs={'profile': profile})

@login_required
def accountsprofile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return HttpResponseRedirect(reverse('userProfile.html', kwargs={'user_id': user.id}))

   

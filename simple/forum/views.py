from django.shortcuts import render, get_object_or_404
from PIL import Image as PImage

from simple.settings import MEDIA_ROOT
from forum.models import Forum
from forum.shared.utils import *
from forum.shared.utils import ContainerFormMixin
from django.forms import ModelForm

from forum.detail import DetailView
from edit import CreateView, UpdateView
from list_custom import ListView, ListRelated

from forms import ProfileForm, PostForm
from django.template.loader import get_template
# Create your views here.

def Main(request):
	forum = Forum.objects.all()
	return render(request, "list.html",)

def ForumView(request):
	forumview = get_object_or_404(forum, pk=forum_title)
	return render(request, 'forum.html', {'forumview':forumview})

def ThreadView(request):
	threadview = get_object_or_404(thread, pk=thread_title)
	return render(request, 'thread.html', {'threadview': threadview})

def EditProfile(request):
	UserProfile = get_object_or_404(UserProfile, pk=User)
	return render(request, 'profile.html', {'editprofile': editprofile})
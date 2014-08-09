from django import forms
from django.forms import ModelForm
from models import *
from forum.shared.utils import ContainerFormMixin

class ProfileForm(forms.Form):
	username = forms.CharField(label='Username', max_length=40)
	first_name = forms.CharField(label='First name', max_length=40)
	last_name = forms.CharField(label='Last name', max_length=40)
	email = forms.CharField(label='Email', max_length=40)
	password = forms.CharField(label='Password', max_length=40, widget=forms.PasswordInput)
	retype_password = forms.CharField(label='Retype password', max_length=40, widget=forms.PasswordInput)

class PostForm(ContainerFormMixin, ModelForm):
	class Meta:
		model   = Post
		exclude = ["creator", "thread"]

class ForumForm(ContainerFormMixin, ModelForm):
	class Meta:
		model   = Forum
		exclude = ["body"]

class ThreadForm(ContainerFormMixin, ModelForm):
	class Meta:
		model   = Thread
		exclude = ["body"]
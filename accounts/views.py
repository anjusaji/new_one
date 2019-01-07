from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView


class UserList(generic.ListView):
	model = User
	template_name = 'accounts/user-list.html'
	context_object_name = 'users'
	
	def get_queryset(self):
		queryset = User.objects.all()
		
		term = self.request.GET.get('term')
		if term:
			queryset = queryset.filter(Q(first_name__icontains=term) | Q(last_name__contains=term))
		
		return queryset


class Home(generic.DetailView):
	model = User
	template_name = 'accounts/home.html'
	context_object_name = 'users_home'


class UserDetail(generic.DetailView):
	model = User
	template_name = 'accounts/user-detail.html'
	context_object_name = 'user_profile'


class Login(LoginView):
	model = User
	template_name = 'accounts/login.html'

	def get_success_url(self):
		return '/tweets/'


class Register(generic.CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'register.html'

from django.views import generic
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django import forms
from django.shortcuts import render
from . forms import LoginForm,RegistrationForm
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from . models import *
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class LoginView(generic.FormView):
	template_name='chimp/login.html'
	form_class=LoginForm
	success_url=reverse_lazy('')

	def get(self, *args, **kwargs):
		if self.request.user:
			print(self.request.user)
			return redirect(self.success_url) 
			#return HttpResponseRedirect("login successfully")
		return super(LoginView, self).get(*args, **kwargs)
		
		
	def form_valid(self,form):
		username =form.cleaned_data.get('username')
		password=form.cleaned_data.get('password')
		user=authenticate(username=username,password=password)
		# import pdb
		# pdb.set_trace()
		if user.is_active:
			login(self.request, user)

class LogoutView(View):
	def get(self,request):
		logout(request)
		messages.success(request, 'logout successfully')
		return HttpResponse("Account logout successfully")

class RegistrationView(generic.FormView):
	template_name='chimp/registration.html'
	form_class=RegistrationForm
	#success_url=reverse_lazy('')
	def form_valid(self,form):
		username=form.cleaned_data.get('username')
		name =form.cleaned_data.get('name')
		#first_name,last_name=split_full_name(full_name)
		password=form.cleaned_data.get('password')
		business_name =form.cleaned_data.get('business_name')
		email=form.cleaned_data.get('email')
		package=form.cleaned_data.get('package')
		#fname=name.split()[0]
		#lname=name.split()[1]
		user=User(username=username, first_name=name,email=email)
		#user.save(commit=False)
		user.set_password(password)
		user.save()
		userprofile=UserProfile(user=user,business_name=business_name,package=package)
		userprofile.save()
		messages.success(self.request, 'User Register Successfully')
		return HttpResponseRedirect('user Register Successfully')

class AddView(SuccessMessageMixin,CreateView):
	model=Campaign
	fields=['name','mailing_list','template']
	template_name='chimp/create.html'
	#success_url='/admin'
	success_url=reverse_lazy('')
	success_message = 'Campaign Created Successfully '
	def form_valid(self, form, *args, **kwargs):
		if form.is_valid():
			campaign = form.save(commit=False)
			campaign.user = self.request.user
			Campaign.save()
		return super(AddView, self).form_valid(form, *args, **kwargs)

class EditView(SuccessMessageMixin, UpdateView):
	model=Campaign
	fields=['name','mailing_list','template']
	template_name='chimp/edit.html'
	success_url = '/admin'
	#success_url=reverse_lazy('blog:dashboard')
	success_message = 'Campaign Edited Successfully'

class AddMailList(SuccessMessageMixin, CreateView):
	model= MailingList
	fields = ['name', 'mailing_list_path']
	#fields = '__all__'
	template_name = 'chimp/add_mail_list.html'
	success_message = 'Mail list added.'
	success_url='/admin'
	def form_valid(self,form, *args, **kwargs):
		if form.is_valid(): 
			mailinglist=form.save(commit=False)
			mailinglist.user=self.request.user
			mailinglist.save()
			return super(AddMailList, self).form_valid(form, *args, **kwargs)
class AddTemplateList(SuccessMessageMixin, CreateView):
	model=TemplateList
	fields= ['image','template_name','category','path']
	template_name='chimp/add_template_list.html'
	success_message='Template list added'
	success_url='/admin'


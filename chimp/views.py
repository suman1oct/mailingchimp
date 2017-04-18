from django.views import generic
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django import forms
from django.shortcuts import render
from . forms import LoginForm,RegistrationForm, AddCampaignForm
from . forms import *
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from . models import *
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.mail import send_mail
from django.http import HttpResponse
from django.views import View
from openpyxl import load_workbook
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse

from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import re

class LoginView(generic.FormView):
	template_name='chimp/login.html'
	form_class=LoginForm
	#success_url=reverse_lazy('chimp:dashboard')
	success_url='chimp:create'
	def get(self, *args, **kwargs):
		if self.request.user:
			#print(self.request.user)
			if self.request.user.is_authenticated():
				redirect('chimp:dashboard')
			#return redirect(self.success_url)
			#return redirect('chimp:dashboard') 
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
			#return redirect('chimp:dashboard')
			return redirect(self.success_url)
class LogoutView(View):
	def get(self,request):
		logout(request)
		messages.success(request, 'logout successfully')
		return redirect('chimp:login')

class RegistrationView(generic.FormView):
	template_name='chimp/registration.html'
	form_class=RegistrationForm
	success_url=reverse_lazy('chimp:dashboard')
	def form_valid(self,form):
		username=form.cleaned_data.get('username')
		name =form.cleaned_data.get('name')
		password=form.cleaned_data.get('password')
		business_name =form.cleaned_data.get('business_name')
		email=form.cleaned_data.get('email')
		package=form.cleaned_data.get('package')
		try:
			user=User(username=username, first_name=name,email=email)
			if User.objects.filter(username=user.username).exists():
				messages.success(self.request,'Username already exist')
				return HttpResponse("User already exist")
		except User.DoesNotExist:
			pass
		user.set_password(password)
		user.save()
		userprofile=UserProfile(user=user,business_name=business_name,package=package)
		userprofile.save()
		messages.success(self.request, 'User Register Successfully')
		return redirect(self.success_url)

class AddView(generic.FormView):
	# model=Campaign
	# fields=['name','mailing_list','template']
	template_name='chimp/create.html'
	success_url='/admin'
	#success_url=reverse_lazy('')
	form_class = AddCampaignForm

	def get_form_kwargs(self):
		kwargs = super(AddView, self).get_form_kwargs()
		kwargs['request'] = self.request
		return kwargs

	def form_valid(self, form, *args, **kwargs):
		if form.is_valid():
			campaign = form.save(commit=False)
			campaign.user = self.request.user
			form.save()
			messages.success(self.request, 'Campaign created  Successfully')
			#Campaign.save()

			"""# msg_plain = render_to_string('templates/email.txt', {'some_params': some_params})
			msg_plain = ''
			#msg_html = render_to_string('<html><body><h1>hello</h1></body></html>')
			msg_html = render_to_string('Campaign.objects.filter(user=self.request.user)__template_list__path')
			receiver = ['some@receiver.com', 'some1@receiver.com', 'some2@receiver.com']
			send_mail('email title',msg_plain, 'some@sender.com', receiver, html_message=msg_html,)
			"""		
		return super(AddView, self).form_valid(form, *args, **kwargs)

class EditView(SuccessMessageMixin, UpdateView):
	model=Campaign
	fields=['name','mailing_list','template']
	template_name='chimp/edit.html'
	success_url = '/admin'
	#success_url=reverse_lazy('')
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





class SendEmailView(View):
	def get(self, request, *args, **kwargs):


		campaign_obj=Campaign.objects.filter(user=self.request.user)[0]
		print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		print(campaign_obj.mailing_list.mailing_list_path)
		path=campaign_obj.mailing_list.mailing_list_path
		template_path=campaign_obj.template.path
		#msg_plain = render_to_string('email.txt', {})
		# wb = load_workbook(filename = 'media/uploads/excels/mailtest.xlsx')
		wb = load_workbook(filename = path)
		sheet = wb.worksheets[0]
		row_count = sheet.max_row
		column_count = sheet.max_column
		users_name=[]
		receiver=[]
		for i in range(2, row_count):
			for j in range(1, column_count):
				users_name.append(sheet.cell(row=i, column=1).value)
				email_id=sheet.cell(row=i, column=2).value
				try:
					if validate_email(email_id):
						receiver.append(sheet.cell(row=i, column=2).value)
				except ValidationError:
					pass

		# sent_mail=len(users_name)
		# print("******************************sent mail*******************************")
		# print(sent_mail)
		# import ipdb; ipdb.set_trace()
		u=UserProfile.objects.get(user=self.request.user)
		
		print(u.sent_email)
		# print("**************************************************************************")
		# c=Campaign.objects.get(user=self.request.user)
		# print(c.mailing_list.mailing_list_path)


		#msg_html = render_to_string('chimp/mail2.html', {})
		import os
		with open(os.getcwd()+template_path.url) as temp_file:
			content = temp_file.readlines()

		print(content)
			
		# msg_html = render_to_string(template_path.url, {'content': self.request.user})
		
		send_mail('email title','subject','sumanymca@gmail.com',receiver,html_message=str(content),)
		return HttpResponse("Email sent succesfuly")

class DashboardView(generic.ListView):
	template_name='chimp/dashboard.html'
	model=Campaign

	def get(self, *args, **kwargs):
		if not self.request.user.is_authenticated():
			return redirect('chimp:login')
		return super(DashboardView, self).get(*args, **kwargs)

	def get_queryset(self):
		return Campaign.objects.filter(user=self.request.user)

class HomepageView(generic.ListView):
	template_name='chimp/homepage.html'
	def get_queryset(self):
		return TemplateList.objects.all()



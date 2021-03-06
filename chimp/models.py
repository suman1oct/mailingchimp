from django.db import models
from django.utils import timezone
from .choices import PACKAGE_CHOICES,CATEGORY_CHOICES



import uuid
import os

def get_file_path():
	pass

def get_mailingfile_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('excels/', filename)

def get_templatesfile_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('templates/', filename)


class MailingList(models.Model):
	name=models.CharField(max_length=100, unique=True)
	user=models.ForeignKey('auth.User', on_delete=models.CASCADE)
	mailing_list_path=models.FileField(upload_to=get_mailingfile_path)
	add_date= models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.name


class Template(models.Model):
	image=models.ImageField(upload_to='images/')
	template_name=models.CharField(max_length=100)
	#category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
	category=models.CharField(max_length=30, choices=CATEGORY_CHOICES, null=False)
	file=models.FileField(upload_to=get_templatesfile_path)
	
	def __str__(self):
		return self.template_name


class Campaign(models.Model):
	user=models.ForeignKey('auth.User',on_delete=models.CASCADE,)
	name=models.CharField(max_length=50,null=True)
	created_date=models.DateTimeField(default=timezone.now)
	mailing_list=models.ForeignKey(MailingList,on_delete=models.CASCADE,)
	template=models.ForeignKey(Template)
	
	def __str__(self):
		return self.name


class UserProfile(models.Model):
	user=models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='profile')
	sent_email=models.IntegerField(default=0)
	remaining_email=models.IntegerField(default=0)
	business_name=models.CharField(max_length=100,null=True)
	package=models.CharField(max_length=10, choices=PACKAGE_CHOICES,null=True,default='BASIC')
	email=models.EmailField(blank=True)
	
	# def __str__(self):
	# 	return self.user

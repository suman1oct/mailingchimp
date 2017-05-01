from django.db import models
from django.utils import timezone
from .choices import PACKAGE_CHOICES,CATEGORY_CHOICES


class MailingList(models.Model):
	name=models.CharField(max_length=100)
	user=models.ForeignKey('auth.User', on_delete=models.CASCADE)
	mailing_list_path=models.FileField(upload_to='excels/')
	
	def __str__(self):
		return self.name


class TemplateList(models.Model):
	image=models.ImageField(upload_to='images/')
	template_name=models.CharField(max_length=100)
	#category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
	category=models.CharField(max_length=10, choices=CATEGORY_CHOICES, null=False)
	file=models.FileField(upload_to='templates/')
	
	def __str__(self):
		return self.template_name


class Campaign(models.Model):
	user=models.ForeignKey('auth.User',on_delete=models.CASCADE,)
	name=models.CharField(max_length=50,null=True)
	created_date=models.DateTimeField(default=timezone.now)
	mailing_list=models.ForeignKey(MailingList,on_delete=models.CASCADE,)
	template=models.ForeignKey(TemplateList)
	
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

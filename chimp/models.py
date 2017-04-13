from django.db import models
from django.utils import timezone

# local import
from .choices import PACKAGE_CHOICES,CATEGORY_CHOICES

#class Category(models.Model):
#	name=models.CharField(max_length=100)


class MailingList(models.Model):
	name=models.CharField(max_length=100)
	user=models.ForeignKey('auth.User', on_delete=models.CASCADE)
	mailing_list_path=models.FileField(upload_to='uploads/excels/')

class TemplateList(models.Model):
	image=models.ImageField(upload_to='uploads/')
	template_name=models.CharField(max_length=100)
	#category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
	category=models.CharField(max_length=10, choices=CATEGORY_CHOICES, null=False)
	path=models.FileField(upload_to='uploads/')


class Campaign(models.Model):
	user=models.ForeignKey('auth.User',on_delete=models.CASCADE,)
	name=models.CharField(max_length=50,null=True)
	
	created_date=models.DateTimeField(default=timezone.now)
	mailing_list=models.ForeignKey(MailingList,on_delete=models.CASCADE,)
	template=models.ForeignKey(TemplateList)


class UserProfile(models.Model):
	user=models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='profile')
	sent_email=models.IntegerField(default=0)
	remaining_email=models.IntegerField(default=0)
	business_name=models.CharField(max_length=100,null=True)
	package=models.CharField(max_length=10, choices=PACKAGE_CHOICES,null=True,default='BASIC')

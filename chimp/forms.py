from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import UserProfile
from .choices import PACKAGE_CHOICES
from .models import Campaign, MailingList
from .validation import validate_fullname ,validateEmail

class LoginForm(forms.Form):					# User Login Form
	username =forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'User name'}))
	password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

	def clean(self):
		username = self.cleaned_data.get('username')
		password= self.cleaned_data.get('password')
		user=authenticate(username=username, password=password)
		if not user or not user.is_active:
			raise forms.ValidationError("Not valid user")
		return self.cleaned_data

class RegistrationForm(forms.Form):				# User Sign Up Form
	username =forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'User name'}))
	name =forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
	password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
	business_name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Business'}))
	email=forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'email id'}), validators=[validateEmail])
	package=forms.CharField(max_length=10,label='Package',widget=forms.Select(choices=PACKAGE_CHOICES),)

	def clean_username(self):
		if User.objects.filter(username=self.cleaned_data['username']).exists():
			raise forms.ValidationError('user already exist')

		return self.cleaned_data['username']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if email and User.objects.filter(email=email).exists():
			raise forms.ValidationError(u'Email addresses must be unique.')
		return email

	def clean(self):
		username = self.cleaned_data.get('username')
		name = self.cleaned_data.get('name')
		business_name =  self.cleaned_data.get('business_name')
		email = self.cleaned_data.get('email')
		password = self.cleaned_data.get('password')
		package = self.cleaned_data.get('package')
		#if User.objects.filter(user=self.cleaned_data['username']).exists():
		#	raise forms.ValidationError('user already exist')
		return self.cleaned_data

class EmailForm(forms.Form):
	from_email=forms.EmailField(required=True)
	#to_email=forms.EmailField(required=True)
	subject=forms.CharField(required=True,max_length=100)
	message=forms.CharField(widget=forms.Textarea)

	def clean(self):
		from_email=self.cleaned_data.get('from_email')
		#to_email=self.cleaned_data.get('from_email')
		subject=self.cleaned_data.get('subject')
		message=self.cleaned_data.get('message')
		return self.cleaned_data

class AddCampaignForm(forms.ModelForm):			# for create a new campaign

	def __init__(self, *args, **kwargs):
		request = kwargs.pop("request")
		super(AddCampaignForm, self).__init__(*args, **kwargs)
		self.fields["mailing_list"].queryset = MailingList.objects.filter(user=request.user)

	class Meta:
		model = Campaign
		fields = ['name','mailing_list','template']


class EditCampaignForm(forms.ModelForm):		# for edit the existing campaign of specific user

	def __init__(self, *args, **kwargs):
		request = kwargs.pop("request")
		super(EditCampaignForm, self).__init__(*args, **kwargs)
		# it will modify the only Mailing_list field of form
		self.fields["mailing_list"].queryset = MailingList.objects.filter(user=request.user)

	class Meta:
		model = Campaign
		fields = ['name','mailing_list','template']



class EditUserProfileForm(forms.Form):				# User Sign Up Form
	username =forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'User name'}))
	name =forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
	password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
	business_name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Business'}))

	def clean_username(self):
		if User.objects.filter(username=self.cleaned_data['username']).exists():
			raise forms.ValidationError('user already exist')

		return self.cleaned_data['username']

	def clean(self):
		username = self.cleaned_data.get('username')
		name = self.cleaned_data.get('name')
		business_name =  self.cleaned_data.get('business_name')
		password = self.cleaned_data.get('password')
		return self.cleaned_data

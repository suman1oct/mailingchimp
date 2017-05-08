from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import UserProfile
from .choices import PACKAGE_CHOICES
from .models import Campaign, MailingList
from .validation import validate_fullname ,validateEmail

class LoginForm(forms.Form):					# User Login Form
	username =forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Username'}))
	password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

	def clean(self):
		username = self.cleaned_data.get('username')
		password= self.cleaned_data.get('password')
		user=authenticate(username=username, password=password)
		if not user or not user.is_active:
			raise forms.ValidationError("Not a Valid Username Or Password")
		return self.cleaned_data

class RegistrationForm(forms.Form):				# User Sign Up Form
	username =forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
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
			raise forms.ValidationError(u'Email address already register.')
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
	name =forms.CharField(max_length=100, widget=forms.TextInput())
	business_name=forms.CharField(max_length=100, widget=forms.TextInput())

	def clean_username(self):
		if User.objects.filter(username=self.cleaned_data['username']).exists():
			raise forms.ValidationError('user already exist')
		return self.cleaned_data['username']


class MailingListForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
    	self.request = kwargs.pop('request', None)
    	super(MailingListForm, self).__init__(*args, **kwargs)
    
    def clean_mailing_list_path(self):
        file_type = self.request.FILES['mailing_list_path'].content_type
        mime_type_list=['application/vnd.ms-excel','application/msexcel','application/x-msexcel','application/x-ms-excel','application/x-excel','application/x-dos_ms_excel','application/xls','application/x-xls','application/vnd.openxmlformats-officedocument.spreadsheetml.sheet','application/vnd.ms-excel.sheet.binary.macroEnabled.12','application/vnd.openxmlformats-officedocument.spreadsheetml.template',]
        if(file_type not in  mime_type_list):
            raise forms.ValidationError('Please upload .xlsx file')
        return self.cleaned_data['mailing_list_path']
    
    class Meta:
        model = MailingList
        fields = ['name','mailing_list_path',]

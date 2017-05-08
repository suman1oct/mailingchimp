from django.contrib import admin
from .models import MailingList, Template, Campaign, UserProfile
from django import forms




class TemplateAdminForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
    	self.request = kwargs.pop('request', None)
    	super(TemplateAdminForm, self).__init__(*args, **kwargs)
    
    def clean_file(self):
        file_type = self.request.FILES['file'].content_type
        if(file_type!='text/html'):
            raise forms.ValidationError('Please upload the HTML file')
        return self.cleaned_data['file']
    
    class Meta:
        model = Template
        fields = ['image','template_name','category','file']


class TemplateAdmin(admin.ModelAdmin):
    form = TemplateAdminForm
    list_display = ('image', 'template_name', 'file')
    search_fields = ('template_name',)
    list_filter=['template_name']

    def get_form(self, request, obj=None, **kwargs):

        AdminForm = super(TemplateAdmin, self).get_form(request, obj, **kwargs)

        class AdminFormWithRequest(AdminForm):
            def __new__(cls, *args, **kwargs):
                kwargs['request'] = request
                return AdminForm(*args, **kwargs)

        return AdminFormWithRequest


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'sent_email', 'remaining_email', 'business_name', 'package')
	search_fields = ('user__first_name','user__last_name')
	list_filter=['user__first_name']


@admin.register(MailingList)
class MailingListAdmin(admin.ModelAdmin):
	list_display = ('name', 'user', 'mailing_list_path')
	search_fields = ('name',)
	list_filter=['name']


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
	list_display = ('user', 'name', 'created_date', 'mailing_list', 'template')
	search_fields = ('user',)
	list_filter=['user',]
	form = TemplateAdminForm


admin.site.register(Template ,TemplateAdmin)



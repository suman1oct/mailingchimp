from django.contrib import admin
from .models import MailingList, TemplateList, Campaign, UserProfile

#admin.site.register(Campaign)
# admin.site.register(UserProfile)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('id','user', 'sent_email', 'remaining_email', 'business_name', 'package')
	search_fields = ('user__first_name','user__last_name')
	list_filter=['user__first_name']

@admin.register(MailingList)
class MailingListAdmin(admin.ModelAdmin):
	list_display = ('name', 'user', 'mailing_list_path')
	search_fields = ('name',)
	list_filter=['name']

@admin.register(TemplateList)
class TemplateListAdmin(admin.ModelAdmin):
	list_display = ('image', 'template_name', 'file')
	search_fields = ('template_name',)
	list_filter=['template_name']

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
	list_display = ('user', 'name', 'created_date', 'mailing_list', 'template')
	search_fields = ('user',)
	list_filter=['user',]

# admin.site.register(MailingList)
# admin.site.register(TemplateList)



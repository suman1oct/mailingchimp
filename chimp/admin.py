from django.contrib import admin
from .models import *

admin.site.register(Campaign)
# admin.site.register(UserProfile)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'sent_email', 'remaining_email', 'business_name', 'package')

admin.site.register(MailingList)
admin.site.register(TemplateList)



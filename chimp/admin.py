from django.contrib import admin

#from .models import Campaign,UserProfile
from .models import *
admin.site.register(Campaign)
admin.site.register(UserProfile)
admin.site.register(MailingList)
admin.site.register(TemplateList)



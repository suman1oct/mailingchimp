from django.conf.urls import url
from . import views

app_name='chimp'

urlpatterns=[
	url(r'^login/', views.LoginView.as_view(), name='login'),
	url(r'^logout/', views.LogoutView.as_view(), name='logout'),
	url(r'^registration/', views.RegistrationView.as_view(), name='registration'),
	url(r'^create/', views.AddCampaignView.as_view(), name='create'),
	url(r'^edit/(?P<pk>[0-9]+)/', views.EditCampaignView.as_view(), name='edit'),
	url(r'^user/add-mail-list/$', views.AddMailList.as_view(), name='add_mail_list'),
	url(r'^user/add-template-list/', views.AddTemplateList.as_view(), name='add_template_list'),
	url(r'^user/send-mail/(?P<pk>\d+)/', views.SendEmailView.as_view(), name='send_mail'),
	url(r'^user/dashboard/', views.DashboardView.as_view(), name='dashboard'),
	url(r'^$', views.HomepageView.as_view(), name='homepage'),
	url(r'^campaign-detail/(?P<pk>\d+)/', views.CampaignDetailView.as_view(), name='campaign_detail'),
	url(r'^show-templates/', views.ShowTemplateView.as_view(), name='show_templates'),
	url(r'^show-mailing-list/', views.ShowMailingListView.as_view(), name='show_mailing_list'),
	url(r'^show-campaign/', views.ShowCampaignView.as_view(), name='show_campaign'),
	url(r'^user-profile/', views.UserProfileView.as_view(), name='user_profile'),
	url(r'^delete-campaign/(?P<pk>[0-9]+)/', views.DeleteCampaignView.as_view(), name='delete_campaign'),
	url(r'^delete-mailing-list/(?P<pk>[0-9]+)/', views.DeleteMailingListView.as_view(), name='delete_mailing_list'),
	
]	
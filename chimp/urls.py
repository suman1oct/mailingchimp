from django.conf.urls import url
from . import views

app_name='chimp'

urlpatterns=[
	url(r'^login/', views.LoginView.as_view(), name='login'),
	url(r'^logout/', views.LogoutView.as_view(), name='logout'),
	url(r'^registration/', views.RegistrationView.as_view(), name='registration'),
	url(r'^create/', views.AddView.as_view(), name='create'),
	url(r'^edit/(?P<pk>[0-9]+)/', views.EditView.as_view(), name='edit'),
	url(r'^user/add-mail-list/$', views.AddMailList.as_view(), name='add_mail_list'),
	url(r'^user/add-template-list/', views.AddTemplateList.as_view(), name='add_template_list'),
	url(r'^user/send-mail/', views.SendEmailView.as_view(), name='send_mail'),
	url(r'^user/dashboard/', views.DashboardView.as_view(), name='dashboard'),
	url(r'^homepage/', views.HomepageView.as_view(), name='homepage'),
	#url(r'^validate-email/', views.validateEmail, name='homepage'),
	

]	
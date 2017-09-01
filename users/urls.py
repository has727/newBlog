from django.conf.urls import url, include
from django.contrib.auth.views import login
from users.views import logout, register


urlpatterns = [
	url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
	url(r'^logout/$', logout, name='logout'),
	url(r'^register/$', register, name='register'),
	
]
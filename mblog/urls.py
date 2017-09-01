from django.conf.urls import url
from mblog.views import index, details, list, addTopic, addEntry, editEntry


urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^list/$', list, name='list'),
	url(r'^details/(?P<topic_id>\d+)/$', details, name='details'),
	url(r'^add_post/$', addTopic, name='addTopic'),
	url(r'^add_entry/(?P<topic_id>\d+)/$', addEntry, name='addEntry'),
	url(r'^edit_entry/(?P<topic_id>\d+)/$', editEntry, name='editEntry'),
	
]
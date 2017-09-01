from django.shortcuts import render, reverse
from mblog.models import Topic, Entry
from datetime import datetime
from mblog.forms import TopicForm, EntryForm
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
	topic = Topic.objects.all()
	now = datetime.now()
	
	context = {'topic': topic, 'now': now}
	return render(request, 'mblog/index.html', context)

@login_required
def list(request):
	topic_list = Topic.objects.all()
	topics = Topic.objects.filter(owner=request.user).order_by('date_added')

	context = {'topic_list': topic_list}
	return render(request, 'mblog/list.html', context)


@login_required
def details(request, topic_id):
	topic = Topic.objects.get(id=topic_id)
	
	entries = topic.entry_set.order_by('-date_added')

	context = {'topic': topic, 'entries': entries}
	return render(request, 'mblog/details.html', context)
	

@login_required
def addTopic(request):
	if request.method != 'POST':
		form = TopicForm()
	else:
		form = TopicForm(request.POST)
		if form.is_valid():
			new_topic = form.save(commit=False)
			new_topic.owner = request.user
			new_topic.save()
			return HttpResponseRedirect(reverse('mblog:list'))
		
	context = {'form': form}
	return render(request, 'mblog/add_post.html', context)


@login_required
def addEntry(request, topic_id):
	topic = Topic.objects.get(id=topic_id)
	
	if request.method != 'POST':
		form = EntryForm()
	else:
		form = EntryForm(request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.owner = request.user
			new_entry.topic = topic
			new_entry.save()
			return HttpResponseRedirect(reverse('mblog:details', args=[topic_id]))
			
	context = {'topic': topic, 'form': form}
	return render(request, 'mblog/add_entry.html', context)


@login_required
def editEntry(request, topic_id):
	entry = Entry.objects.get(id=topic_id)
	topic = entry.topic
	
	if topic.owner != request.user:
		return render(request, 'mblog/index.html')
	
	if request.method != 'POST':
		form = EntryForm(instance=entry)
	else:
		form = EntryForm(instance=entry, data=request.POST)
		if form.is_valid():
			edit_entry = form.save(commit=False)
			edit_entry.owner = request.user
			edit_entry.save()
			return HttpResponseRedirect(reverse('mblog:details', args=[topic_id]))
	
	context = {'entry': entry, 'topic': topic, 'form': form}
	return render(request, 'mblog/edit_entry.html', context)

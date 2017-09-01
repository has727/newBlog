from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout as lgout, login as lgin, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def logout(request):
	lgout(request)
	return HttpResponseRedirect(reverse('mblog:index'))


def register(request):
	if request.method != 'POST':
		form = UserCreationForm()
	else:
		form = UserCreationForm(data=request.POST)
		
		if form.is_valid():
			new_user = form.save()
			authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
			lgin(request, authenticated_user)
			return HttpResponseRedirect(reverse('mblog:index'))
		
	context = {'form': form}
	return render(request, 'users/register.html', context)


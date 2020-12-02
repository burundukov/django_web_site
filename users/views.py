from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserWithEmail
from django.contrib.auth.decorators import login_required

def register(request):
	if request.method == "POST":
		form = UserWithEmail(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Пользователь {username} был успешно создан.')
			return redirect('top')
	else:	
		form = UserWithEmail()
	return render(request, 'users/registration.html', {'form': form, 'title': 'Регистрация пользователя'})


@login_required
def profile(request):
	return render(request, 'users/profile.html')
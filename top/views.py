from django.shortcuts import render
from .models import Post

def home(request):
	data = {
		'info': Post.objects.all(),
		'title': "Главная страница сайта",
	}
	return render(request, 'top/index.html', data)


def about(request):
	return render(request, 'top/about.html', {'title': "Страница о нас."})

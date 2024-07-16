from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Films
from .forms import NewFilmForm


# Create your views here.
def index(request):
    films = Films.objects.all()
    return render(request, 'films/index.html', {'films': films})  # Указываем правильный путь к шаблону


def added(request):
	error = ''
	if request.method == 'POST':
		form = NewFilmForm(request.POST) # Сюда сохранится информация от пользователя.
		if form.is_valid():
			form.save()
			return redirect('index')
		else:
			error = "Данные были заполнены некорректно"
	form = NewFilmForm()
	return render(request, 'films/added.html', {'form': form, 'error': error})
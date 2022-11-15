from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie
from .models import Uyelik
from .models import Program


def index(request):
    return render(request, 'index.html', {"name":"home"})

def about(request):
    searchTerm = request.GET.get('searchMovie')
    movies = Program.objects.all()
    return render(request, 'about.html', {'Program':Program})

def classes(request):
    return render(request, 'classes.html', {"name":"classes"})

def contact(request):
    return render(request, 'contact.html', {"name":"contact"})

def schedule(request):
    return render(request, 'schedule.html', {"name":"schedule"})

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email':email})

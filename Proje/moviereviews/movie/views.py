from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {"name":"Murat"})
def about(request):
    return HttpResponse("<h1>Welcome to About Page</h1>")

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email':email})

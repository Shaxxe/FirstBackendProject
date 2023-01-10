from django.shortcuts import render, get_object_or_404
from .models import Uyelik
from .models import Program
from .models import Trainer
from .models import Class
from django.views.generic import DetailView


def index(request):
    Trainers = Trainer.objects.all()
    return render(request, 'index.html', {"name":"index", 'Trainers':Trainers})

def about(request):
    Trainers = Trainer.objects.all()
    searchTerm = request.GET.get('searchMovie')
    Programs = Program.objects.all()
    return render(request, 'about.html', {"name":"about", 'Programs':Programs, 'Trainers':Trainers})

def classes(request):
    Trainers = Trainer.objects.all()
    Classes = Class.objects.all()
    return render(request, 'classes.html', {"name":"classes", 'Trainers':Trainers, 'Classes':Classes})

def schedule(request):
    Classes = Class.objects.all()
    Trainers = Trainer.objects.all()
    return render(request, 'schedule.html', {"name":"schedule", 'Trainers':Trainers, 'Classes':Classes})

def signup(request):
    Trainers = Trainer.objects.all()
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email':email, 'Trainers':Trainers})




class MyModelDetailView(DetailView):   
    quaryset = Program.objects.all()
    template_name = 'program_detail.html' 
    Programs = Program.objects.all()
    Trainers = Trainer.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Program, Program_id=id_)


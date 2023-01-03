from django.core.mail import send_mail
from django.shortcuts import render, redirect
from movie.models import Trainer
from django.contrib import messages
from .forms import Contactform


def contact(request):
    if request.method == 'POST':
        form = Contactform(request.POST)
        
        if form.is_valid():
            name =request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            send_mail(name, message, email,['muratozturk3734@hotmail.com'])
            messages.success(request, 'Mesaj gönderildi!')
            
            return redirect('contact')
        
    else:
        form = Contactform()
    Trainers = Trainer.objects.all()
    return render(request, 'contact.html',{"name":"contact",'form': form,'Trainers':Trainers})
from django.db import models
from django.contrib.auth.models import User
from django.views.generic import DetailView

DAYS_OF_WEEK = (
    (0, 'Monday'),
    (1, 'Tuesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
    (5, 'Saturday'),
    (6, 'Sunday'),
)



class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='movie/static/images/')
    url = models.URLField(blank=True)


class Uyelik(models.Model):
    Uyelik_turu = models.IntegerField(primary_key = True)
    Uyelik_date = models.DateField()
    Uyelik_name = models.CharField(max_length=250)
    Uyelik_url = models.URLField(blank=True,null=True)

    def __str__(self):
        return self.Uyelik_name

class Person(models.Model):
    Person_id = models.IntegerField(primary_key = True)
    Person_name = models.CharField(max_length=250)
    Person_lastname = models.CharField(max_length=250)
    Person_email = models.EmailField(max_length=100,blank=True,unique=False)
    Person_image = models.ImageField(upload_to='movie/static/images/')
    Uyelik_turu = models.ForeignKey(Uyelik,on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.Person_name

class Trainer(models.Model):
    Trainer_id = models.IntegerField(primary_key = True)
    Trainer_name = models.CharField(max_length=100)
    Trainer_lastname = models.CharField(max_length=350)
    Trainer_img = models.ImageField(upload_to='movie/static/images')
    Trainer_desc = models.CharField(max_length=160)
    Person_email = models.ForeignKey(Person,on_delete=models.CASCADE, null = True)
    Trainer_fb = models.URLField(null=True, blank=True)
    Trainer_tw = models.URLField(null=True, blank=True)
    Trainer_ln = models.URLField(null=True, blank=True)
    Trainer_type = models.CharField(max_length=20)

    def __str__(self):
        return self.Trainer_name

class Program(models.Model):
    Program_id = models.IntegerField(primary_key = True)
    Program_title = models.CharField(max_length=100)
    Program_description = models.CharField(max_length=50)
    Program_about = models.CharField(max_length=5000)
    Program_img = models.ImageField(upload_to='movie/static/images')
    Trainer_id = models.ForeignKey(Trainer,on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.Program_title


class Class(models.Model):
    Class_id = models.IntegerField(primary_key = True)
    Class_name = models.CharField(max_length=50)
    Class_desc = models.CharField(max_length=500)
    Class_dayOfTheWeek = models.IntegerField(choices=DAYS_OF_WEEK)
    Class_finishingtime = models.TimeField(verbose_name ='Time') #Sınıfın Bitiş Saati
    Class_beginningtime = models.TimeField(verbose_name ='Time') #Sınıfın Başlangıç Saati
    Class_img = models.ImageField(upload_to='movie/static/images')
    Program_id = models.ForeignKey(Program,on_delete=models.CASCADE, null = True)
    Trainer_name = models.ForeignKey(Trainer, null = True, on_delete=models.CASCADE)

    def __str__(self):
        return self.Class_name


class MyModelDetailView(DetailView):
    model = Program
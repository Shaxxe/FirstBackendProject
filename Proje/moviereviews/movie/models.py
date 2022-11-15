from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='movie/static/images/')
    url = models.URLField(blank=True)

class Uyelik(models.Model):
    Uyelik_turu = models.IntegerField(primary_key = True)
    Uyelik_date = models.DateField(auto_now_add=True)
    Uyelik_url = models.URLField(blank=True)

class Person(models.Model):
    Person_id = models.IntegerField(primary_key = True)
    Person_name = models.CharField(max_length=250)
    Person_lastname = models.CharField(max_length=250)
    Person_email = models.EmailField(max_length=100,blank=True,unique=False)
    Person_image = models.ImageField(upload_to='movie/static/images/')
    Uyelik_turu = models.ForeignKey(Uyelik,on_delete=models.CASCADE)

class Trainer(models.Model):
    Trainer_id = models.IntegerField(primary_key = True)
    Trainer_name = models.CharField(max_length=100)
    Trainer_lastname = models.CharField(max_length=350)
    Trainer_img = models.ImageField(upload_to='movie/static/images')
    Trainer_email = models.EmailField(max_length=70,blank=True,unique=False)
    Person_id = models.ForeignKey(Person,on_delete=models.CASCADE)


class Program(models.Model):
    Program_id = models.IntegerField(primary_key = True)
    Program_title = models.CharField(max_length=100)
    Program_description = models.CharField(max_length=350)
    Trainer_id = models.ForeignKey(Trainer,on_delete=models.CASCADE)


class Class(models.Model):
    Class_id = models.IntegerField(primary_key = True)
    Class_date = models.DateField(auto_now_add=True)
    Class_time = models.TimeField(verbose_name ='Time')
    Program_id = models.ForeignKey(Program,on_delete=models.CASCADE)

class Schedule(models.Model):
    Class_date = models.ForeignKey(Class,on_delete=models.CASCADE)
    Trainer_id = models.ForeignKey(Trainer,on_delete=models.CASCADE)

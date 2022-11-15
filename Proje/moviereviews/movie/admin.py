from django.contrib import admin

from .models import Movie
from .models import Uyelik
from .models import Program

admin.site.register(Movie)
admin.site.register(Uyelik)
admin.site.register(Program)
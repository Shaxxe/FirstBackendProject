from django.contrib import admin

from .models import Movie
from .models import Uyelik
from .models import Program
from .models import Trainer
from .models import Person
from .models import Class

admin.site.register(Movie)
admin.site.register(Uyelik)
admin.site.register(Program)
admin.site.register(Trainer)
admin.site.register(Person)
admin.site.register(Class)
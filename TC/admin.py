from django.contrib import admin

# Register your models here.
from .models import Matiers1

admin.site.register(Matiers1)

from .models import Archivetc

admin.site.register(Archivetc)


# admin.py
from django.contrib import admin

class Archivetc(admin.ModelAdmin):
    list_display = ('title', 'pdf_file')

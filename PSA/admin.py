from django.contrib import admin

# Register your models here.
from .models import Matierpsa

admin.site.register(Matierpsa)

from .models import Archivepsa

admin.site.register(Archivepsa)


# admin.py
from django.contrib import admin

class Archivetc(admin.ModelAdmin):
    list_display = ('title', 'pdf_file')

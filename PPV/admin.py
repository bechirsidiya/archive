from django.contrib import admin

# Register your models here.
from .models import Matierppv

admin.site.register(Matierppv)

from .models import Archiveppv

admin.site.register(Archiveppv)


# admin.py
from django.contrib import admin

class Archivetc(admin.ModelAdmin):
    list_display = ('title', 'pdf_file')

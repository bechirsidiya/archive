from django.contrib import admin

# Register your models here.
from .models import Matiersta

admin.site.register(Matiersta)

from .models import Archivesta

admin.site.register(Archivesta)


# admin.py
from django.contrib import admin

class Archivetc(admin.ModelAdmin):
    list_display = ('title', 'pdf_file')

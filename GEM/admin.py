from django.contrib import admin

# Register your models here.
from .models import Matiergm

admin.site.register(Matiergm)

from .models import Archivegm

admin.site.register(Archivegm)


# admin.py
from django.contrib import admin

class Archivegm(admin.ModelAdmin):
    list_display = ('title', 'pdf_file')

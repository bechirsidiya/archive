from django.contrib import admin

# Register your models here.
from .models import Matiergab

admin.site.register(Matiergab)

from .models import Archivegab

admin.site.register(Archivegab)
admin.site.site_header='l archive de l ISET'
admin.site.site_title = 'l archive de l ISET'

# admin.py
from django.contrib import admin

class Archivetc(admin.ModelAdmin):
    list_display = ('title', 'pdf_file')

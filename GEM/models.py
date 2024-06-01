from django.db import models
from django.contrib.auth.models import User

class Matiergm(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)

    def __str__(self):
   
        return self.name


class Archivegm(models.Model):
    matiergm =models.ForeignKey(Matiergm, related_name='archive' ,on_delete= models.CASCADE) 
    title = models.CharField(max_length=100)
    pdf_file = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.title
from django.db import models

# Create your models here.
class Docente(models.Model):
    nombre = models.CharField(max_length=100)
    profesion = models.CharField(max_length=100)
    linkedin = models.URLField(blank=True)
    foto = models.ImageField(upload_to='docentes/')

    def __str__(self):
        return self.nombre
    


class Estudiantes(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    profesion = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='estudiantes/')

    def __str__(self):
        return self.nombre


class HistoriaVideo(models.Model):
    nombre = models.CharField("Nombre", max_length=200)
    video = models.FileField("Video", upload_to='historias/')
    reel = models.URLField("Enlace al Reel", blank=True, null=True)

    def __str__(self):
        return self.nombre





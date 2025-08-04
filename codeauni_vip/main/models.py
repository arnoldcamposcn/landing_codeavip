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
    nombre = models.CharField("Nombre", max_length=200, blank=True, null=True)  # <- ahora no requerido
    video = models.FileField("Video", upload_to='historias/', blank=True, null=True)  # <- no requerido
    reel = models.URLField("Enlace al Reel", blank=True, null=True)  # ya estaba opcional

    def __str__(self):
        return self.nombre or "Sin nombre"




class DocenteBusiness(models.Model):
    nombre = models.CharField(max_length=100)
    profesion = models.CharField(max_length=100)
    linkedin = models.URLField(blank=True)
    foto = models.ImageField(upload_to='docentes/')

    def __str__(self):
        return self.nombre



class EstudiantesBusiness(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    profesion = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='estudiantes/')

    def __str__(self):
        return self.nombre
    

class HistoriaVideoBusiness(models.Model):
    nombre = models.CharField("Nombre", max_length=200, blank=True, null=True)  # <- ahora no requerido
    video = models.FileField("Video", upload_to='historias/', blank=True, null=True)  # <- no requerido
    reel = models.URLField("Enlace al Reel", blank=True, null=True)  # ya estaba opcional

    def __str__(self):
        return self.nombre or "Sin nombre"



class MembresiaFormulario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    pais = models.CharField(max_length=100)
    especializacion = models.CharField(max_length=50)
    perfil = models.CharField(max_length=20)
    membresia = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.membresia} membresía(s)"
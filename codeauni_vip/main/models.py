from django.db import models

# Create your models here.
class Docente(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    profesion = models.CharField(max_length=100, blank=True, null=True)
    especialidad = models.CharField(max_length=100, blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    foto = models.ImageField(upload_to='docentes/', blank=True)

    def __str__(self):
        return self.nombre or "Sin nombre"
    
    class Meta:
        verbose_name = "docentes"
        verbose_name_plural = "docentes"
    

class Clientes(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    profesion = models.CharField(max_length=100, blank=True, null=True)
    foto = models.ImageField(upload_to='clientes/', blank=True)

    def __str__(self):
        return self.nombre or "Sin nombre"
    
    class Meta:
        verbose_name = "clientes"
        verbose_name_plural = "clientes"


class HistoriaVideoBusiness(models.Model):
    video = models.FileField("Video", upload_to='historias/', blank=True, null=True)
    reel = models.URLField("Enlace al Reel", blank=True, null=True)

    def __str__(self):
        return f"HistoriaVideoBusiness #{self.id}"
    
    class Meta:
        verbose_name = "Historia_videos_business"
        verbose_name_plural = "Historia_videos_business"



class marcas_bussines(models.Model):
    imagen = models.ImageField(upload_to='marcas/', blank=True)

    def __str__(self):
        return f"Marca {self.id}"



class membresia_estudiantes(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    pais = models.CharField(max_length=100)
    especializacion = models.CharField(max_length=50)
    membresia = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.membresia} membresía(s)"
    


class membresia_profesionales(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    pais = models.CharField(max_length=100)
    especializacion = models.CharField(max_length=50)
    membresia = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.membresia} membresía(s)"
    

class prueba_gratuita_vip(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    pais = models.CharField(max_length=100)
    especializacion = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    


class membresia_bussines(models.Model):
    PLANES_MEMBRESIA = (
        (1, 'Membresía 2-10'),
        (2, 'Membresía 11-100'),
        (3, 'Membresía +100'),
    )

    nombre_empresa = models.CharField(max_length=150)
    nombre_encargado = models.CharField(max_length=100)
    sitio_web = models.URLField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    pais = models.CharField(max_length=100)
    membresia = models.IntegerField(choices=PLANES_MEMBRESIA, default=1)

    class Meta:
        verbose_name = "Membresía Business"
        verbose_name_plural = "Membresías Business"
        ordering = ['nombre_empresa']

    def __str__(self):
        return f"{self.nombre_empresa} - {self.get_membresia_display()}"
    

class membresia_free_bussines(models.Model):
    nombre_empresa = models.CharField(max_length=150)
    nombre_encargado = models.CharField(max_length=100) 
    sitio_web = models.URLField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    pais = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre_empresa} - {self.nombre_encargado}"



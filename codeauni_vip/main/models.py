from django.db import models
from decimal import Decimal
from django.core.exceptions import ValidationError

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


def validar_tamano_video(value):
    limit_mb = 5
    if value.size > limit_mb * 1024 * 1024:
        raise ValidationError(f"El tamaño máximo permitido es {limit_mb} MB")
    
class HistoriaVideoBusiness(models.Model):
    video = models.FileField(
        "Video",
        upload_to='historias/',
        blank=True,
        null=True,
        validators=[validar_tamano_video]  # 👈 Aquí aplicamos el validador
    )

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



class MembresiaVIP(models.Model):
    etiqueta_cabecera = models.CharField(max_length=100, blank=True, null=True)
    nombre = models.CharField("Nombre de la membresía", max_length=100)
    precio = models.DecimalField("Precio base", max_digits=10, decimal_places=2)
    beneficios = models.TextField("Beneficios", help_text="Lista de beneficios, separados por saltos de línea.",blank=True, null=True)
    oferta = models.CharField("Oferta especial", max_length=100, blank=True, null=True, help_text="Ej: Descuento, Black Friday, etc.")

    class Meta:
        verbose_name = "Membresía VIP"
        verbose_name_plural = "Membresías VIP"
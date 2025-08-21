from django.db import models
from multiselectfield import MultiSelectField
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
from PIL import Image
import os

class TipoContenido(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "tipo_de_contenido"


def validate_image_file(value):
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.webp']
    ext = os.path.splitext(value.name)[1].lower()
    
    if ext not in valid_extensions:
        raise ValidationError(
            f'Formato de archivo no soportado. Use: {", ".join(valid_extensions)}'
        )
    
    try:
        image = Image.open(value)
        image.verify()
        
        if value.size > 3 * 1024 * 1024:  
            raise ValidationError('El archivo no debe exceder 3MB')
            
    except Exception as e:
        raise ValidationError('El archivo no debe exceder 3MB')


class Tema(models.Model):
    titulo = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo



class Curso(models.Model):
    ENTREGA_CHOICES = [
        ('', 'Seleccionar'),
        ('ondemand', 'On Demand'),
        ('envivo', 'En Vivo'),
    ]

    DIAS_SEMANA = [
        ('lunes', 'Lunes'),
        ('martes', 'Martes'),
        ('miercoles', 'Miércoles'),
        ('jueves', 'Jueves'),
        ('viernes', 'Viernes'),
        ('sabado', 'Sábado'),
        ('domingo', 'Domingo'),
    ]

    titulo = models.CharField(max_length=200)
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE, related_name='cursos')
    descripcion = models.TextField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True,
        help_text="Enlace video"
    )

    
    tipo_entrega = models.CharField(
        max_length=20,
        choices=ENTREGA_CHOICES,
        blank=True,
        null=True,
        default=''
    )
    
    tipo_contenido = models.ForeignKey(
        TipoContenido,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='cursos'
    )

    dias_disponibles = MultiSelectField(
        choices=DIAS_SEMANA,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.titulo
    
    
    mostrar_en_vip = models.BooleanField(
        default=False,
        verbose_name="Mostrar en VIP",
    )
    mostrar_en_business = models.BooleanField(
        default=False,
        verbose_name="Mostrar en Business",
    )

    

class TipoModulo(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True, blank=True)
    nombre_modulo = models.CharField(max_length=100)
    descripcion_modulo = models.TextField(blank=True, null=True)
    orden = models.IntegerField (blank=True, null=True, default=0)

    def __str__(self):
        return self.nombre_modulo

    class Meta:
        verbose_name = "crear_modulo"



class Temario(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='temarios')
    tipo_modulo = models.ForeignKey(
        TipoModulo,
        on_delete=models.CASCADE,
        related_name='temarios'
    )
    capitulo = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)

    


    def __str__(self):
        return self.capitulo
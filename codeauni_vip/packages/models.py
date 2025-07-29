from django.db import models
from multiselectfield import MultiSelectField


class Tema(models.Model):
    titulo = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo


class Capitulo(models.Model):
    ENTREGA_CHOICES = [
        ('', 'Seleccionar'),
        ('ondemand', 'On Demand'),
        ('envivo', 'En Vivo'),
    ]

    CONTENIDO_CHOICES = [
        ('', 'Seleccionar'),
        ('masterclass', 'Masterclass'),
        ('curso', 'Curso'),
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
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE, related_name='capitulos')
    
    tipo_entrega = models.CharField(
        max_length=20,
        choices=ENTREGA_CHOICES,
        blank=True,
        null=True,
        default=''
    )
    
    tipo_contenido = models.CharField(
        max_length=20,
        choices=CONTENIDO_CHOICES,
        blank=True,
        null=True,
        default=''
    )

    dias_disponibles = MultiSelectField(
        choices=DIAS_SEMANA,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.titulo} ({self.tema.titulo})"
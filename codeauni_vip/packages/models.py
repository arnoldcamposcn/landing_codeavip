from django.db import models
from multiselectfield import MultiSelectField


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
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE, related_name='cursos')
    
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

    

class Temario(models.Model):
    MODULO_CHOICES = [
        ('modulo_1', 'Módulo 1'),
        ('modulo_2', 'Módulo 2'),
        ('modulo_3', 'Módulo 3'),
        ('modulo_4', 'Módulo 4'),
    ]

    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='temarios')
    capitulo = models.CharField(max_length=255)  # Título del capítulo
    descripcion = models.TextField(blank=True)   # Descripción corta o larga de la clase
    tipo_modulo = models.CharField(max_length=20, choices=MODULO_CHOICES)

    orden = models.PositiveIntegerField(default=0)  # Para ordenar los capítulos dentro del módulo

    class Meta:
        ordering = ['tipo_modulo', 'orden']

    def __str__(self):
        return f"{self.capitulo} ({self.get_tipo_modulo_display()} - {self.curso.titulo})"


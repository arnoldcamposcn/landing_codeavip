from django.db import models
from multiselectfield import MultiSelectField

class TipoContenido(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "tipo_de_contenido"


class Tema(models.Model):
    titulo = models.CharField(max_length=200)
    portada = models.ImageField(upload_to='portada/', blank=True)


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
        return f"{self.titulo} ({self.tema.titulo})"
    
    
    mostrar_en_vip = models.BooleanField(
        default=False,
        verbose_name="Mostrar en VIP",
    )
    mostrar_en_business = models.BooleanField(
        default=False,
        verbose_name="Mostrar en Business",
    )

    

class TipoModulo(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "crear_modulo"



class Temario(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='temarios')
    capitulo = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    tipo_modulo = models.ForeignKey(
        TipoModulo,
        on_delete=models.CASCADE,
        related_name='temarios'
    )

    def __str__(self):
        return f"{self.capitulo} ({self.tipo_modulo.nombre} - {self.curso.titulo})"

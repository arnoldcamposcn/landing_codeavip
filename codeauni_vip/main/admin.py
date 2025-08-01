from django.contrib import admin
from .models import Docente, HistoriaVideo, Estudiantes, DocenteBusiness, EstudiantesBusiness,HistoriaVideoBusiness 

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'profesion', 'linkedin', 'foto')

@admin.register(Estudiantes)
class EstudiantesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'profesion', 'foto')

@admin.register(HistoriaVideo)
class HistoriaVideoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'video', 'reel')
    search_fields = ('nombre',)





@admin.register(DocenteBusiness)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'profesion', 'linkedin', 'foto')

@admin.register(EstudiantesBusiness)
class EstudiantesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'profesion', 'foto')

@admin.register(HistoriaVideoBusiness)
class HistoriaVideoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'video', 'reel')
    search_fields = ('nombre',)


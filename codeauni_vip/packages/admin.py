from django.contrib import admin
from .models import Tema, Curso, Temario

@admin.register(Tema)
class TemaAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    search_fields = ('titulo',)


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tema', 'tipo_entrega', 'tipo_contenido')
    search_fields = ('titulo',)
    list_filter = ('tema', 'tipo_entrega', 'tipo_contenido')

    class Media:
        js = ('js/conditional_fields_chapter.js',) 


@admin.register(Temario)
class TemarioAdmin(admin.ModelAdmin):
    list_display = ('curso', 'capitulo', 'tipo_modulo', 'orden')
    list_filter = ('curso', 'tipo_modulo')
    search_fields = ('capitulo', 'descripcion')
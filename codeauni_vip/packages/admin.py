from django.contrib import admin
from .models import Tema, Curso, Temario, TipoContenido, TipoModulo

@admin.register(Tema)
class TemaAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    search_fields = ('titulo',)



@admin.register(TipoContenido)
class TipoContenidoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)



@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tema', 'video_url', 'tipo_entrega', 'tipo_contenido', 'mostrar_en_vip', 'mostrar_en_business')
    search_fields = ('titulo',)
    list_filter = ('tema', 'tipo_entrega', 'tipo_contenido', 'mostrar_en_vip', 'mostrar_en_business')
    autocomplete_fields = ['tema']
    class Media:
        js = ('js/conditional_fields_chapter.js',) 
        


@admin.register(Temario)
class TemarioAdmin(admin.ModelAdmin):
    list_display = ('capitulo', 'curso', 'tipo_modulo', 'descripcion')
    list_filter = ('curso', 'tipo_modulo')
    autocomplete_fields = ('curso',)
    
    
    class Media:
        js = ('js/temario_cascada.js',)


@admin.register(TipoModulo)
class TipoModuloAdmin(admin.ModelAdmin):
    list_display = ('nombre_modulo','descripcion_modulo','orden', 'curso')     
    autocomplete_fields = ['curso']

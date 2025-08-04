from django.contrib import admin
from .models import Tema, Capitulo

class TemaAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    search_fields = ('titulo',)

admin.site.register(Tema, TemaAdmin)

class CapituloAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tema', 'tipo_entrega', 'tipo_contenido')
    search_fields = ('titulo',)
    list_filter = ('tema', 'tipo_entrega', 'tipo_contenido')

    class Media:
        js = ('js/conditional_fields_chapter.js',) 



admin.site.register(Capitulo, CapituloAdmin)


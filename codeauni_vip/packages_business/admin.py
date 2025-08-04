from django.contrib import admin
from .models import TemaBusiness, CapituloBusiness


class TemaBusinessAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    search_fields = ('titulo',)


class CapituloBusinessAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tema', 'tipo_entrega', 'tipo_contenido')
    search_fields = ('titulo',)
    list_filter = ('tema', 'tipo_entrega', 'tipo_contenido')

    class Media:
        js = ('js/conditional_fields_chapter.js',)  # Asegúrate de que el JS esté cargando correctamente


admin.site.register(TemaBusiness, TemaBusinessAdmin)
admin.site.register(CapituloBusiness, CapituloBusinessAdmin)

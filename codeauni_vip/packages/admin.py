from django.contrib import admin
from .models import Tema, Capitulo, TemaBusiness, CapituloBusiness
class TemaAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    search_fields = ('titulo',)

admin.site.register(Tema, TemaAdmin)

class CapituloAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tema', 'tipo_entrega', 'tipo_contenido')
    search_fields = ('titulo',)
    list_filter = ('tema', 'tipo_entrega', 'tipo_contenido')


admin.site.register(Capitulo, CapituloAdmin)


# Nuevos admin para Business

class TemaBusinessAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    search_fields = ('titulo',)

admin.site.register(TemaBusiness, TemaBusinessAdmin)


class CapituloBusinessAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tema', 'tipo_entrega', 'tipo_contenido')
    search_fields = ('titulo',)
    list_filter = ('tema', 'tipo_entrega', 'tipo_contenido')

admin.site.register(CapituloBusiness, CapituloBusinessAdmin)
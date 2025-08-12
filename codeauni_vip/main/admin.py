from django.contrib import admin
from .models import MembresiaVIP, Docente, Clientes,HistoriaVideoBusiness, marcas_bussines


@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'profesion', 'linkedin', 'foto')


@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'profesion', 'foto')


@admin.register(HistoriaVideoBusiness)
class HistoriaVideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'video')


@admin.register(marcas_bussines)
class marcas_bussinesAdmin(admin.ModelAdmin):
    list_display = ('imagen',)  


@admin.register(MembresiaVIP)
class MembresiaVIPAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'oferta', 'beneficios', 'etiqueta_cabecera')
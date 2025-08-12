from django.contrib import admin
from .models import Docente, Clientes,HistoriaVideoBusiness, marcas_bussines


@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'profesion', 'linkedin', 'foto')


@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'profesion', 'foto')


@admin.register(HistoriaVideoBusiness)
class HistoriaVideoAdmin(admin.ModelAdmin):
    list_display = ('video', 'reel')


@admin.register(marcas_bussines)
class marcas_bussinesAdmin(admin.ModelAdmin):
    list_display = ('imagen',)  
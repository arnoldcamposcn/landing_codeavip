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
    list_display = ('video', 'reel')


@admin.register(marcas_bussines)
class marcas_bussinesAdmin(admin.ModelAdmin):
    list_display = ('imagen',)  



@admin.register(MembresiaVIP)
class MembresiaVIPAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'descuento', 'precio_final_display')
    list_filter = ('descuento',)
    search_fields = ('nombre', 'beneficios')

    def precio_final_display(self, obj):
        """Muestra el precio final en el admin."""
        return f"${obj.precio_final:.2f}"
    precio_final_display.short_description = 'Precio Final'
from django.contrib import admin
from gestionPedidos.models import Clientes 
from gestionPedidos.models import Articulos
from gestionPedidos.models import Pedidos
# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre","direccion","telefono", "email")
    search_fields=("nombre", "telefono")
admin.site.register(Clientes ,ClientesAdmin)


class ArticulosAdmin(admin.ModelAdmin):
    list_filter=("seccion","precio")
    search_fields=("nombre", "seccion")
    
admin.site.register(Articulos,ArticulosAdmin)
    

class PedidosAdmin(admin.ModelAdmin):
    list_display=("numero","fecha")
    list_filter=("fecha",)
    date_hierarchy="fecha"
    
    
admin.site.register(Pedidos,PedidosAdmin)   
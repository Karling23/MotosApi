from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    Usuario, Marca, Categoria, Motocicleta, Casco, Accesorio,
    Pedido, DetallePedido, Pago, Testing
)

@admin.register(Usuario)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Información Adicional', {'fields': ('telefono', 'direccion', 'rol')}),
    )
    list_display = ['username', 'email', 'first_name', 'last_name', 'rol', 'is_staff']
    list_filter = ['rol', 'is_staff', 'is_superuser', 'is_active']

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'pais_origen', 'activo']
    search_fields = ['nombre']

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'activo']
    search_fields = ['nombre']

@admin.register(Motocicleta)
class MotocicletaAdmin(admin.ModelAdmin):
    list_display = ['marca', 'modelo', 'anio', 'cilindrada', 'precio', 'stock']
    list_filter = ['marca', 'categoria', 'anio']
    search_fields = ['modelo', 'descripcion']

@admin.register(Casco)
class CascoAdmin(admin.ModelAdmin):
    list_display = ['marca', 'modelo', 'talla', 'color', 'precio', 'stock']
    list_filter = ['marca', 'talla']
    search_fields = ['modelo', 'certificacion']

@admin.register(Accesorio)
class AccesorioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'marca', 'categoria_accesorio', 'precio', 'stock']
    list_filter = ['marca', 'categoria_accesorio']
    search_fields = ['nombre']

class DetallePedidoInline(admin.TabularInline):
    model = DetallePedido
    extra = 1

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'fecha_pedido', 'estado', 'total']
    list_filter = ['estado', 'fecha_pedido']
    search_fields = ['usuario__username']
    inlines = [DetallePedidoInline]

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ['id', 'pedido', 'metodo_pago', 'monto', 'estado', 'fecha_pago']
    list_filter = ['estado', 'metodo_pago', 'fecha_pago']
    search_fields = ['transaccion_id']

@admin.register(Testing)
class TestingAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'motocicleta', 'fecha_test', 'estado']
    list_filter = ['estado', 'fecha_test']
    search_fields = ['usuario__username', 'motocicleta__modelo']

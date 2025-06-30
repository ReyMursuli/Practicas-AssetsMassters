from django.contrib import admin
from .models import Area,Activo
from django.utils.html import mark_safe

# Register your models here.
class ActivoAdmin(admin.ModelAdmin):
    list_display=('cod_interno','rotulo','mostrar_qr')

    def mostrar_qr(self,obj):
        if obj.qr_code:
            return mark_safe(f'<img src="{obj.qr_code.url}" whidth="100" heigth="100" />')
        return "No generado"

    mostrar_qr.short_descripcion="Codigo QR"

    
admin.site.register(Area)
admin.site.register(Activo,ActivoAdmin)
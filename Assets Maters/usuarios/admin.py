from django.contrib import admin
from .models import UsuarioGenerico, Responsable

class UsuarioGenericoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    fields = ('nombre', 'contrasenya')
    
    def save_model(self, request, obj, form, change):
        raw_password = form.cleaned_data.get('contrasenya')
        if raw_password and not raw_password.startswith('pbkdf2_'):
            obj.set_password(raw_password)
        super().save_model(request, obj, form, change)

class ResponsableAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo')
    fields = ('nombre', 'contrasenya', 'codigo')

    def save_model(self, request, obj, form, change):
        raw_password = form.cleaned_data.get('contrasenya')
        if raw_password and not raw_password.startswith('pbkdf2_'):
            obj.set_password(raw_password)
        super().save_model(request, obj, form, change)

admin.site.register(UsuarioGenerico, UsuarioGenericoAdmin)
admin.site.register(Responsable, ResponsableAdmin)
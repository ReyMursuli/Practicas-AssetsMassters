from django.db import models
from django.contrib.auth.hashers import make_password,check_password 

      
class UsuarioGenerico(models.Model):
        nombre=models.CharField(max_length=60)  
        contrasenya=models.CharField(max_length=50)
        
        def set_password(self,raw_password):
            self.contrasenya = make_password(raw_password)
            self.save()
            
        def check_password(self,raw_password):
            return check_password(raw_password,self.contrasenya)    
        
        class Meta():
            verbose_name='Usuario'
            verbose_name_plural='Usuarios'
            
        def __str__(self):
            return self.nombre
            
 
        
class Responsable(UsuarioGenerico):
    codigo = models.CharField(max_length=20)
    
    class Meta:
        verbose_name="Responsable"
        verbose_name_plural="Responsable de los activos"
        
        
    def __str__(self):
        return self.nombre                       
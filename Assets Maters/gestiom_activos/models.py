from django.db import models
from django.conf import settings
from usuarios.models import Responsable
import qrcode
from io import BytesIO
from django.core.files import File
from .utils import generar_nombre_qr

# Create your models here.
class Area(models.Model):
    nombre = models.CharField(max_length=150)
    codigo = models.CharField(max_length=150)
    
class Activo(models.Model):
    cod_interno=models.CharField(max_length=50,unique=True)
    rotulo = models.CharField(max_length=50) 
    nombre =models.CharField(max_length=255)
    tipo = models.CharField(max_length=250)
    descripcion =models.CharField(max_length=250)
    valor_inicial=models.DecimalField(max_digits=12,decimal_places=2)
    valor_residual=models.DecimalField(max_digits=12,decimal_places=2)
    depen_acomulada=models.DecimalField(max_digits=12,decimal_places=2)
    qr_code = models.ImageField(upload_to='qrcodes',blank=True,null=True)
    
    area=models.ForeignKey(Area,on_delete=models.CASCADE,related_name='activos')
    responsable=models.ForeignKey(Responsable,on_delete=models.SET_NULL,null=True,blank=True,related_name='activos_asignados')
    
    def __str__(self):
        return f"{self.cod_interno}-{self.nombre}"
    
    
    def save (self,*args,**kwargs):
        super(Activo,self).save(*args,**kwargs)
        
        if not self.qr_code:
            qr=qrcode.make(f"Activo:{self.cod_interno}-{self.nombre}")
            buffer=BytesIO()
            qr.save(buffer,fromat='PNG')
            nombre_archivo=generar_nombre_qr(self.cod_interno)
            self.qr_code.save(nombre_archivo,File=buffer,save=False)
            super(Activo,self).save(*args, **kwargs)
    
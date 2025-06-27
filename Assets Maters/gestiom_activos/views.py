from django.shortcuts import render,get_object_or_404
from .models import Activo,Area
from usuarios.models import Responsable


def listar_activos(request):
    activos=Activo.objects.all()
    return render(request,'gestiom_activos/lista_activos.html',{'activos',activos})

def activos_por_area(request,area_id):
    area=get_object_or_404(Area,id=area_id)
    activos=Activo.objects.filter(area=area)
    return render(request,'gestiom_activos/activos_por_area.html',{'area':area},{'activos':activos})

def elegir_area(request):
    areas=Area.objects.all()
    return render(request,'gestiom_activos/elegir_area.html',{'areas':areas})  

def activos_por_responsable(request,jefe_id):
    responsables=get_object_or_404(Responsable,id=jefe_id)
    activos=Activo.objects.filter(responsables=responsables)
    return render(request,'gestiom_activos/activos_por_responsable.html',{'jefe':responsables,'activos':activos})

def elegir_responsable(request):
    responsables=Responsable.objects.all()    
    return render(request,'gestiom_activos/elegir_responsable.html',{'respnsables':responsables}) 

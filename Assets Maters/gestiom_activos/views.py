from django.shortcuts import render,get_object_or_404
from .models import Activo,Area
from usuarios.models import Responsable
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import  os
from django.urls import reverse
from django.shortcuts import redirect
from django.db import models

def listar_activos(request):
    activos=Activo.objects.all()
    return render(request,'gestion_activos/listar_activos.html',{'activos':activos})

def listar_areas(request):
    areas = Area.objects.all()
    return render(request, 'gestion_activos/lista_areas.html', {'areas': areas})

def activos_por_area(request,area_id):
    area=get_object_or_404(Area,id=area_id)
    activos=Activo.objects.filter(area=area)
    return render(request,'gestion_activos/activos_por_area.html',{'area':area},{'activos':activos})

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

def generar_reporte_pdf(request):
    activos = Activo.objects.all()
    template_path = 'activos_pdf.html'
    context = {'activos': activos}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="activos.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Error al generar el PDF', status=500)
    return response

def controlar_activos(request):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('login')

    from usuarios.models import Responsable
    try:
        responsable = Responsable.objects.get(id=usuario_id)
    except Responsable.DoesNotExist:
        return HttpResponse('No tienes permisos para controlar activos.', status=403)

    # Filtro por tipo o descripción
    query = request.GET.get('q', '').strip()
    activos = Activo.objects.filter(responsable=responsable)
    if query:
        activos = activos.filter(
            models.Q(tipo__icontains=query) | models.Q(descripcion__icontains=query)
        )

    resultado = None

    if request.method == 'POST':
        encontrados = request.POST.getlist('encontrado')
        encontrados = set(map(int, encontrados))
        resultado = {
            'encontrados': [a for a in activos if a.id in encontrados],
            'no_encontrados': [a for a in activos if a.id not in encontrados]
        }
    return render(request, 'controlar_activos.html', {
        'activos': activos,
        'resultado': resultado
    })



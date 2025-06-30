from django.shortcuts import render,redirect
from django.contrib import messages
from .models import UsuarioGenerico
from gestiom_activos.models import Activo


# Create your views here.
def login_view(request):
    if request.method =='POST':
        nombre=request.POST.get('nombre')
        contrasenya=request.POST.get('contrasenya')
        
        try:
            usuario=UsuarioGenerico.objects.get(nombre=nombre)
            if usuario.check_password(contrasenya):
                request.session['usuario_id']=usuario.id
                messages.success(request,'Login Exitoso')
                return redirect('dashboard')
            else:
                messages.error(request,'Contraseña Incorrecta')
        except UsuarioGenerico.DoesNotExist:
            messages.error(request,'Usuario no encontrado')
    
    return render(request,'login.html')
    
def logout_view(request):
    try:
        del request.session['usuario_id']
    except KeyError:
        pass
    messages.info(request,'Sesion cerrada')
    return redirect('login')

def cambiar_contrasenya(request):
    if 'usuario_id' not in request.session:
        return redirect('login')
    usuario=UsuarioGenerico.objects.get(id=request.session['usuario_id']) 
    
    if request.method =='POST':
        actual=request.POST['actual']
        nueva = request.POST['nueva']
        
        if usuario.check_password(actual):
            usuario.set_password(nueva)
            messages.success(request,'Contrasenya actualizada')
            return redirect('home') 
        else:
            messages.error(request,'Contaseña actual incorrecta')
            
    return render(request,'cambiar_contrasenya.html')

def dashboard_view(request):
    usuario_id = request.session.get('usuario_id')

    if not usuario_id:
        return redirect('login')

    usuario = UsuarioGenerico.objects.get(id=usuario_id)

    if hasattr(usuario, 'responsable'):
        responsable = usuario.responsable
        activos = Activo.objects.filter(responsable=responsable)
        return render(request, 'responsable_dashboard.html', {'usuario': usuario, 'activos': activos})
    else:
        return render(request, 'dashboard.html', {'usuario': usuario})
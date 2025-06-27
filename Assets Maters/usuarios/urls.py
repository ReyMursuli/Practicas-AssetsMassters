from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('cambiar-contraseña/',views.cambiar_contrasenya,name='cambiar_contrasenya'),
    path('home/',views.home,name='home'),
     
]

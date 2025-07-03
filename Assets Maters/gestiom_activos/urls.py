from django.urls import path
from . import views


app_name='gestiom_activos'
urlpatterns = [
    path('exportar_pdf/', views.generar_reporte_pdf, name='generar_reporte_pdf'),
    path('controlar_activos/', views.controlar_activos, name='controlar_activos'),
    path('listar_activos/', views.listar_activos, name='listar_activos'),
    path('areas/', views.listar_areas, name='listar_areas'),
    path('areas/<int:area_id>/', views.activos_por_area, name='activos_por_area'),
]
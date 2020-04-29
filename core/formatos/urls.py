from django.urls import path
from django.conf.urls import url
from core.formatos.views import FormulariosIndex, Format_Sintomas, Crear_Nuevo_Formato, Lista_Formatos_Sintomas

app_name = 'formatos'

urlpatterns = [
    path('', FormulariosIndex, name='IndexFormatos'),
    path('sintomas/', Format_Sintomas, name='Crear_Formato_Sintomas'),
    path('sintomas/lista', Lista_Formatos_Sintomas, name='Lista_Formatos_Generados'),
    url(r'^sintomas/guardar/$', Crear_Nuevo_Formato, name='Guardar_Formato_Sintomas'),
]

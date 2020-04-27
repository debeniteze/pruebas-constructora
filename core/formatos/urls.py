from django.urls import path
from django.conf.urls import url
from core.formatos.views import FormulariosIndex, Format_Sintomas, validate_username

app_name = 'formatos'

urlpatterns = [
    path('', FormulariosIndex, name='IndexFormatos'),
    path('sintomas/', Format_Sintomas, name='FormatoSintomas'),
    url(r'^sintomas/guardar/$', validate_username, name='GuardarSintomas'),
]

from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import JsonResponse
from core.formatos.models import Guarda_Reporte_Condiciones_Salud
from django.views.generic import CreateView
from config.settings import sheet_path, sheet_path2, ruta_imagenes_firmas
import json
import openpyxl
import base64
import time
import datetime
from base64 import b64encode

from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def FormulariosIndex(request):
    return render(request, 'IndexFormatos.html', context=None)


def Format_Sintomas(request):
    return render(request, 'Sintomas.html', context=None)


@csrf_exempt
def validate_username(request):
    if request.is_ajax:
        parametros = json.loads(request.body.decode("utf-8"))
        Guarda_Reporte_Condiciones_Salud(parametros)
        arcFirmaTrabajador = parametros["usuarioPruebaRealizada"]+'.jpg'
        arcFirmaInspector = parametros["inspectorSST"]+'.jpg'
        arcFirmEncargado = parametros["encargadoObra"]+'.jpg'

        GuardaFirmas(arcFirmaTrabajador,
                     base64.b64decode(parametros["firmaTrabajador"]))
        GuardaFirmas(arcFirmEncargado,
                     base64.b64decode(parametros["firmaEncargadoObra"]))
        GuardaFirmas(arcFirmaInspector,
                     base64.b64decode(parametros["firmaInspectorObra"]))

        CrearArchivoExcel(arcFirmaTrabajador, arcFirmaInspector, arcFirmEncargado,
                          parametros["usuarioPruebaRealizada"], parametros)
        data = {
            'success': True
        }
    else:
        print('error')
    return JsonResponse(data)


def GuardaFirmas(nombreImagen, dataImagen):
    filename = nombreImagen
    with open(filename, 'wb') as f:
        f.write(dataImagen)


def CrearArchivoExcel(firmaTrabajador, firmaInspector, firmaEncargado, cedulaTrabajador, parametros):
    book = openpyxl.load_workbook(sheet_path)
    sheet = book.active

    trabajador = openpyxl.drawing.image.Image(
        ruta_imagenes_firmas + firmaTrabajador)
    inspector = openpyxl.drawing.image.Image(
        ruta_imagenes_firmas + firmaInspector)
    encargado = openpyxl.drawing.image.Image(
        ruta_imagenes_firmas + firmaEncargado)

    x = datetime.datetime.now()
    sheet['f3'] = "%s" % x.day
    sheet['l3'] = "%s" % x.month
    sheet['y3'] = "%s" % x.year
    sheet['z5'] = parametros["preguntaUno"]
    sheet['z6'] = parametros["preguntaDos"]
    sheet['z7'] = parametros["preguntaTres"]
    sheet['z9'] = parametros["PreguntaCuatro"]
    sheet['z11'] = parametros["preguntaCinco"]
    sheet['z13'] = parametros["preguntaSeis"]
    sheet['z15'] = parametros["preguntaSiete"]
    sheet['z17'] = parametros["preguntaOcho"]
    sheet['z19'] = parametros["preguntaNueve"]
    sheet['z21'] = parametros["preguntaDiez"]
    sheet['z22'] = parametros["totalPuntaje"]
    sheet['g27'] = parametros["temperatura"]
    sheet['a30'] = parametros["nombreCompleto"]
    sheet['q30'] = parametros["cedulaVisitante"]
    sheet['b31'] = parametros["eps"]
    sheet['k31'] = parametros["afp"]
    sheet['u31'] = parametros["arl"]
    sheet['g32'] = parametros["nombrePersonaContacto"]
    sheet['u32'] = parametros["telefonoPersonaContacto"]
    sheet['c33'] = parametros["parentesco"]
    sheet['o33'] = parametros["dondeVive"]
    sheet['a36'] = parametros["encargadoObra"]
    sheet['g36'] = parametros["usuarioPruebaRealizada"]
    sheet['r36'] = parametros["inspectorSST"]
    sheet['a41'] = parametros["observaciones"]

    encargado.anchor = 'A37'
    trabajador.anchor = 'G37'
    inspector.anchor = 'R37'
    sheet.add_image(encargado, 'A37')
    sheet.add_image(trabajador, 'g37')
    sheet.add_image(inspector, 'r37')
    aa = sheet_path2 + "Formato_Trabajador_"+cedulaTrabajador+".xlsx"
    book.save(aa)

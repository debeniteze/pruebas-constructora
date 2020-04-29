from django.db import models, connection
from django.forms import model_to_dict
# Create your models here.


class ReporteCondicionesSalud(models.Model):

    fechaDiligenciamiento = models.DateField("Fecha Diligenciamiento")
    preguntaUno = models.IntegerField("Presenta Tos")
    preguntaDos = models.IntegerField("Presenta Escalofrio")
    preguntaTres = models.IntegerField("Presenta Dolor de Garganta")
    PreguntaCuatro = models.IntegerField("Presenta Dolor Corporal")
    preguntaCinco = models.IntegerField("Presenta Dolor de Cabeza")
    preguntaSeis = models.IntegerField("Presenta Fiebre Mayor a 37.8")
    preguntaSiete = models.IntegerField("Presenta Perdida del Olfato")
    preguntaOcho = models.IntegerField("Presenta Dificulta para Respirar")
    preguntaNueve = models.IntegerField("Presenta Fatiga")
    preguntaDiez = models.IntegerField("Has acompado a alguien con COVID-19")
    puntajeTotal = models.IntegerField("Total Puntaje")
    temperatura = models.IntegerField("Grado de Temperatura")
    observaciones = models.CharField(
        "Observaciones SGSST o Encargado Salud", max_length=5000)
    usuarioPruebaRealizada = models.IntegerField(
        "Funcionario a Realizar Prueba")
    firmaUsuarioPrueba = models.CharField(
        "Firma Quien Realizo", max_length=1000000, null=True, blank=True)
    encargadoObra = models.IntegerField("Encargado Obra")
    firmaEncargadoObra = models.CharField(
        "Firma Encargado Obra", max_length=1000000, null=True, blank=True)
    inspectorSST = models.IntegerField("Inspector SST")
    firmaInspectorObra = models.CharField(
        "Firma Inspecto Obra", max_length=1000000, null=True, blank=True)
    nombreArchivoGenerado = models.CharField(
        "Nombre Archivo Generado XLSX", max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'ReporteCondicionSalud'
        verbose_name_plural = 'ReportesCondicionesSalud'
        ordering = ['id']


class Visitante(models.Model):
    nombreCompleto = models.CharField("Nombre Visitante", max_length=50)
    cedulaVisitante = models.FloatField("Cedula Visitante")
    eps = models.CharField("EPS", max_length=50)
    afp = models.CharField("AFP", max_length=50)
    arl = models.CharField("ARL", max_length=50)
    nombrePersonaContacto = models.CharField(
        "Nombre Contacto Visitante", max_length=50)
    telefonoPersonaContacto = models.CharField(
        "Telefono Contacto Visitante", max_length=50)
    parentesco = models.CharField("Parentesco Con Visitante", max_length=50)
    dondeVive = models.CharField("Donde Vive", max_length=50)

    def __str__(self):
        return self.app_name

    def toJSON(self):
        items - model_to_dict(self)
        return items


def Guarda_Reporte_Condiciones_Salud(parametros, nombre_Archivo):
    with connection.cursor() as cursor:
        cursor.callproc('Guarda_Reporte_Condiciones_Salud', (parametros["preguntaUno"],
                                                             parametros["preguntaDos"],
                                                             parametros["preguntaTres"],
                                                             parametros["PreguntaCuatro"],
                                                             parametros["preguntaCinco"],
                                                             parametros["preguntaSeis"],
                                                             parametros["preguntaSiete"],
                                                             parametros["preguntaOcho"],
                                                             parametros["preguntaNueve"],
                                                             parametros["preguntaDiez"],
                                                             parametros["totalPuntaje"],
                                                             parametros["temperatura"],
                                                             parametros["observaciones"],
                                                             parametros["usuarioPruebaRealizada"],
                                                             parametros["encargadoObra"],
                                                             parametros["inspectorSST"],
                                                             parametros["firmaEncargadoObra"],
                                                             parametros["firmaTrabajador"],
                                                             parametros["firmaInspectorObra"],
                                                             parametros["nombreCompleto"],
                                                             parametros["cedulaVisitante"],
                                                             parametros["eps"],
                                                             parametros["afp"],
                                                             parametros["arl"],
                                                             parametros["nombrePersonaContacto"],
                                                             parametros["telefonoPersonaContacto"],
                                                             parametros["parentesco"],
                                                             parametros["dondeVive"],
                                                             nombre_Archivo))

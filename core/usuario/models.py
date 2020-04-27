from django.contrib.auth.models import AbstractUser
from django.db import models
from config.settings import MEDIA_URL, STATIC_URL
# Create your views here.


class Usuario(AbstractUser):
    imagenPerfil = models.ImageField(upload_to='imgUsuario/%y/%m/%d')
    cargo = models.CharField("Cargo Funcionario", max_length=200,
                             help_text="Campo Obligatorio", unique=True,
                             null=True, blank=True)
    cedula = models.FloatField("Numero Documento", null=True, blank=True)
    celular = models.FloatField("Numero Celular", null=True, blank=True)

    def obtener_imagen(self):
        if self.imagenPerfil:
            return '{}'.format(self.imagenPerfil)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

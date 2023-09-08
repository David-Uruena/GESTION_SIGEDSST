from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Empresa(models.Model):
    nombre_empresa = models.CharField(max_length=80, verbose_name="Nombre Empresa")
    nit = models.CharField(max_length=20, verbose_name="NIT Empresa")
    rut = models.CharField(max_length=20, verbose_name="RUT Empresa", null=True, blank=True)
    nombre_contacto = models.CharField(max_length=60, verbose_name="Nombre Contacto")
    correo = models.EmailField(max_length=150, verbose_name='Correo')
    telefono = models.CharField(max_length=20, verbose_name="Teléfono")
    direccion = models.CharField(max_length=70, verbose_name="Dirección")
    img_logo = models.ImageField(upload_to='img/empresas',
                             blank=True, default='images/empresas/default-150x150.png')
    class Estado(models.TextChoices):
        ACTIVO = '1', _('Activo')
        INACTIVO = '0', _('Inactivo')
    estado = models.CharField(
        max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

    def __str__(self) -> str:
        return "%s" % (self.nombre_empresa)


class Usuario(models.Model):
    nombres = models.CharField(max_length=60, verbose_name="Nombres")
    apellidos = models.CharField(max_length=60, verbose_name="Apellidos")
    image_user = models.ImageField(upload_to='img/usuarios',
                             blank=True, default='img/usuarios/default-150x150.png')
    class TipoDocumento(models.TextChoices):
        CC = 'CC', _('Cédula de Ciudadanía')
        CE = 'CE', _('Cédula de Extranjería')
        OT = 'Otro', _('Otro Tipo de Documento')
    tipoDocumento = models.CharField(
        max_length=4, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo de Documento")
    documento = models.CharField(
        max_length=50, verbose_name="Número de Documento")
    id_profesional = models.CharField(
        max_length=20, verbose_name="Número de Licencia Profesional")
    telefono = models.CharField(max_length=20, verbose_name="Teléfono")
    direccion = models.CharField(max_length=70, verbose_name="Dirección")
    email= models.EmailField(max_length=150, verbose_name='Correo')
    
    class Cargo_SST(models.TextChoices):
        Ingeniero = 'Ingeniero', _('Ingeniero')
        Inspector = 'Inspector', _('Inspector')
        Auxiliar = 'Auxiliar', _('Auxiliar')
    cargo_sst = models.CharField(max_length=9, choices=Cargo_SST.choices,
                           default=Cargo_SST.Ingeniero, verbose_name="Cargo SST")
    
    class Estado(models.TextChoices):
        ACTIVO = '1', _('Activo')
        INACTIVO = '0', _('Inactivo')
    estado = models.CharField(
        max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return "%s %s" % (self.nombres, self.apellidos)
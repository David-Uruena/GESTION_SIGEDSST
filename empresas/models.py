from django.db import models
from empleados.models import Empleado
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

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
    
    class CargoSST(models.TextChoices):
        Ingeniero = 'Ingeniero', _('Ingeniero')
        Inspector = 'Inspector', _('Inspector')
        Auxiliar = 'Auxiliar', _('Auxiliar')
    cargo_sst = models.CharField(max_length=9, choices=CargoSST.choices,
                           default=CargoSST.Ingeniero, verbose_name="Cargo SST")

    estado_usuario = models.BooleanField(max_length=1, default=1, verbose_name="Estado")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return "%s %s" % (self.nombres, self.apellidos)
    

class Inspeccion(models.Model):
    nombre_inspeccion = models.CharField(max_length=60, verbose_name="Nombre inspeccion") 
    descripcion = models.CharField(max_length=250, verbose_name="Nombre descripcion")
    estado_insp = models.BooleanField(max_length=1, default=1, verbose_name="Estado")
    
    def __str__(self) -> str:
        return "%s" % (self.nombre_inspeccion)
 

class ChequeoInspecciones(models.Model):
    fecha_inicio=models.DateTimeField(auto_now=True,verbose_name="Fecha inicio" , help_text=u"MM/DD/AAAA")    
    fecha_fin=models.DateTimeField(auto_now=True,verbose_name="Fecha fin" ,help_text=u"MM/DD/AAAA") 
    
    class InspeccionRealizada(models.TextChoices):
        si = 'si', _('si')
        no = 'no', _('no')
        no_aplica= 'no-aplica', _('no_aplica')
    inspeccion_realizada = models.CharField(max_length=9,
                           choices=InspeccionRealizada.choices,
                           default=InspeccionRealizada.si, verbose_name="Inspección realizada") 
    observaciones = models.CharField(max_length=240, verbose_name="Observaciones")



class EmpleadoChequeoInspecciones(models.Model):
    id_chequeo_inspe=models.ForeignKey(ChequeoInspecciones, on_delete=models.CASCADE, verbose_name="ChequeoInspecciones", related_name="chequeoInspeccionesId")
    id_empleado=models.ForeignKey(Empleado, on_delete=models.CASCADE, verbose_name="Empleado", related_name="EmpleadoCheqInsp")
    encargado_SST = models.BooleanField(default=False, verbose_name="Encargado_SST")


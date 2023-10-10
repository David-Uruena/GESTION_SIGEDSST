from django.db import models
from accidente_enfermedad.models import Accidentes
from django.utils.translation import gettext_lazy as _

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
    estado = models.BooleanField(max_length=1, default=1, verbose_name="Estado")

    def __str__(self) -> str:
        return "%s" % (self.nombre_empresa)

class PermisoTrabajo(models.Model):
    fecha_inicio=models.DateTimeField(auto_now=True,verbose_name="Fecha inicio" , help_text=u"MM/DD/AAAA")    
    fecha_fin=models.DateTimeField(auto_now=True,verbose_name="Fecha fin" ,help_text=u"MM/DD/AAAA") 
    nombre_actividad=models.CharField(max_length=60, verbose_name="Nombre inspeccion") 
        
    class EvaluaRiesgo(models.TextChoices):
        si = 'si', _('si')
        no = 'no', _('no')
    evalua_riesgo = models.CharField(max_length=2, choices=EvaluaRiesgo.choices, default=EvaluaRiesgo.si, verbose_name="Evalua Riesgo")
    
    class PermisoCancelado(models.TextChoices):
        si = 'si', _('si')
        no = 'no', _('no')
    estado = models.CharField(
        max_length=2, choices=PermisoCancelado.choices, default=PermisoCancelado.si, verbose_name="permiso cancelado")
    
    motivo_cancelacion=models.CharField(max_length=120, blank=True, verbose_name="motivo cancelacion")
    id_empresa=models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name="Empresaid", related_name="Empresa_PermisoTrrabajo")   
        
    def __str__(self) -> str:
      return "%s" % (self.nombre_actividad)
  
  
class Cargo(models.Model):
    cargo=models.TextField(max_length=45, verbose_name="cargo")
    funciones=models.TextField(max_length=240, verbose_name="funciones") 
     
class Empleado(models.Model):
    nombres = models.CharField(max_length=45, verbose_name="Nombres")
    apellidos = models.CharField(max_length=45, verbose_name="Apellidos")
    correo = models.EmailField(max_length=45, verbose_name='Correo')
    telefono = models.CharField(max_length=45, verbose_name="Teléfono")
    
    class TipoDocumento(models.TextChoices):
        CC = 'CC', _('Cédula de Ciudadanía')
        CE = 'CE', _('Cédula de Extranjería')
        OT = 'Otro', _('Otro Tipo de Documento')
    tipoDocumento = models.CharField(max_length=4, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo de Documento")
    num_Documento = models.CharField(
        max_length=4, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Número de Documento") 
    cargo=models.ForeignKey(Cargo, on_delete=models.CASCADE, verbose_name="Cargo", related_name="Cargo_Empleado")
    id_empresa=models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name="Empresa", related_name="Empresa_Empleado")
    estado_empl = models.BooleanField(max_length=1, default=1, verbose_name="Estado")
    
class Capacitacion(models.Model):
    fecha_inicio=models.DateTimeField(auto_now=True,verbose_name="Fecha Inicio" , help_text=u"MM/DD/AAAA")
    lugar= models.CharField(max_length=45, verbose_name="Lugar")
    tema_capacitacion= models.CharField(max_length=80, verbose_name="Tema")
    id_empleado=models.ForeignKey(Empleado, on_delete=models.CASCADE, verbose_name="Empleado", related_name="Empleado_Capacitacion")
    
class AusentismoEmpleado(models.Model):
    fecha_inicio=models.DateTimeField(auto_now=True,verbose_name="Fecha Inicio", help_text=u"MM/DD/AAAA")    
    fecha_fin=models.DateTimeField(auto_now=True,verbose_name="Fecha Fin" ,help_text=u"MM/DD/AAAA") 
    descripcion=models.CharField(max_length=240, verbose_name="Descripción")
        
    class TiposAusentismo(models.TextChoices):
        Justificado = 'Justificado', ('Justificado')
        Injustificado = 'Injustificado', ('Injustificado')
    tipos_ausentismo = models.CharField(max_length=13, choices=TiposAusentismo.choices,
                           default=TiposAusentismo.Justificado ,verbose_name="Tipo Ausentismo")
    id_empleado=models.ForeignKey(Empleado, on_delete=models.CASCADE, verbose_name="Empleado", related_name="Empleado_Ausentismo")
    
class EmpleadoAccidentes(models.Model):
    id_empleado=models.ForeignKey(Empleado, on_delete=models.CASCADE, verbose_name="Empleado", related_name="EmpleadoAccidente")
    id_accidentes=models.ForeignKey(Accidentes, on_delete=models.CASCADE, verbose_name="Accidentes", related_name="AccidentesEmpleado")
    encargado_sst = models.BooleanField(default=False, verbose_name="Encargado_SST")






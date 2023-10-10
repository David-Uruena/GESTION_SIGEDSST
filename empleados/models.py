from django.db import models
import accidente_enfermedad
from empresas.models import Empresa
from django.utils.translation import gettext_lazy as _

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
    cargo=models.ForeignKey(Cargo, on_delete=models.CASCADE, verbose_name="Cargo", related_name="Cargo Empleado")
    id_empresa=models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name="Empresa", related_name="Empresa_Empleado")
    
    
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
    tipos_ausentismo = models.CharField(max_length=9, choices=TiposAusentismo.choices,
                           default=TiposAusentismo.Justificado ,verbose_name="Tipo Ausentismo")
    id_empleado=models.ForeignKey(Empleado, on_delete=models.CASCADE, verbose_name="Empleado", related_name="Empleado_Ausentismo")
    
class EmpleadoAccidente(models.Model):
    id_empleado_accidente=models.ForeignKey(EmpleadoAccidente, on_delete=models.CASCADE, verbose_name="EmpleadoAccidente", related_name="EmpleadoAccidente")
    id_accidente=models.ForeignKey(Accidente, on_delete=models.CASCADE, verbose_name="Accidente", related_name="Accidente")
    encargado_sst = models.BooleanField(default=False, verbose_name="Encargado_SST")
        
        

    
    
    
    
 
    
 
    




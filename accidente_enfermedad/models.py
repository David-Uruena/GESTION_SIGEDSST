from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator

class EntidadResponsable(models.Model):
    nombres = models.CharField(max_length=45, verbose_name="Nombres")
    correo = models.EmailField(max_length=45, verbose_name="Correo")
    telefono = models.CharField(max_length=45, verbose_name="Teléfono")
    nombrecontacto= models.CharField(max_length=120, verbose_name="Nombre contacto")
    direccionatenccion = models.CharField(max_length=70, verbose_name="Dirección Atención")
    estado_tinyint = models.BooleanField(max_length=1, default=1, verbose_name="Estado")
    
class CausasAccidente(models.Model):
    nombre_causas=models.CharField(max_length=45, verbose_name="nombre causas")
    
class Accidentes(models.Model):
    fecha_accidente=models.DateTimeField(auto_now=True,verbose_name="Fecha Accidente" , help_text=u"MM/DD/AAAA")
    dias_incapacidad = models.IntegerField(validators=[MinValueValidator(0)],default=0, verbose_name="Días Incapacidad")    
    
    class IncapacidadRemunerada(models.TextChoices):
        si = 'si', _('si')
        no = 'no', _('no')
    incapacidadremunerada = models.CharField(max_length=2, choices=IncapacidadRemunerada.choices, default=IncapacidadRemunerada.si, verbose_name="Incapacidad Remunerada")
    
    class AccidenteMortal(models.TextChoices):
        Caida = 'Caída', _('Caída') 
        Electrocuciones= 'Electrocuciones', _('Electrocuciones')
        Golpes = "Golpes", _("Golpes") 
        Atrapados = "Atrapados", _("Atrapados")
        Otro = "Otro", _("Otro")
    accidentes_mortales= models.CharField(max_length=15, choices=AccidenteMortal.choices, default=AccidenteMortal.Caida, verbose_name="Accidente Mortal")
    odservaciones=models.TextField(max_length=240, verbose_name="Observaciones")
    id_entidadresponable= models.ForeignKey(EntidadResponsable, on_delete=models.CASCADE, verbose_name="Entidad responsable", related_name="accidente_entidadesresponsables")
    id_causa_accidente= models.ForeignKey(CausasAccidente, on_delete=models.CASCADE, verbose_name="Causa accidente", related_name="accidente_causa")

class OrigenEnfermedadLaboral(models.Model):
    nombreorigen=models.CharField(max_length=45, verbose_name="Origen")
    descripcion=models.CharField(max_length=240, verbose_name="Descripcion")

class EnfermedadLaboral(models.Model):
    fecha_inicio=models.DateTimeField(auto_now=True, verbose_name="Fecha Inicio" , help_text=u"MM/DD/AAAA")
    origen_enfermedad=models.ForeignKey(OrigenEnfermedadLaboral, on_delete=models.CASCADE, verbose_name="Causa Enfermedad", related_name="enfermedad_causa")
        
    class ReporteEntidad(models.TextChoices):
         si = 'si', _('si')
         no = 'no', _('no')
    reporte_entidad = models.CharField(max_length=2, choices=ReporteEntidad.choices, default=ReporteEntidad.si, verbose_name="Reporte Entidad")
    entidad_responsable=models.ForeignKey(EntidadResponsable, on_delete=models.CASCADE, verbose_name="Entidad Responsable", related_name="entidad_responsab")
        
    class SeguimientoProfesionalSST(models.TextChoices):
         si = 'si', _('si')
         no = 'no', _('no')
    Seguimientoprofesionalsst = models.CharField(max_length=2, choices=SeguimientoProfesionalSST.choices, default=SeguimientoProfesionalSST.si, verbose_name="Seguimiento Profesional SST")
    odservaciones=models.TextField(max_length=240, verbose_name="Observaciones")
    
class EmpleadoEnfermedadLaboral(models.Model):
    from empleados.models import Empleado
    id_enfermedad_laboral=models.ForeignKey(EnfermedadLaboral, on_delete=models.CASCADE, verbose_name="EnfermedadLaboral", related_name="EnfermedadLaboral")
    id_empleado=models.ForeignKey(Empleado, on_delete=models.CASCADE, verbose_name="Empleado", related_name="Empleado")
    encargado_sst = models.BooleanField(default=False, verbose_name="Encargado_SST")


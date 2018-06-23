from django.db import models
from django.utils.translation import ugettext_lazy as _

class Socio(models.Model):
    # Atributos propios del Socio
    nombre = models.CharField(_('Nombres'), max_length=80)
    apellido = models.CharField(_('Apellidos'), max_length=80)
    cedula = models.BigIntegerField(_('Cedula'))
    
    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)


class Capital(models.Model):
    # Atributos propios del Capital
    socio = models.OneToOneField(Socio, on_delete=models.CASCADE)    
    monto_disponible = models.FloatField(_('Monto Disponible'))
    tasa = models.FloatField(_('Tasa de Interes'), max_length=80)
    
    class Meta:
        ordering = ["-id"]
        verbose_name = 'Capital'
        verbose_name_plural = 'Capital'

    def __str__(self):
        return '%s %s aporta %s con una tasa del %s' % (self.socio.nombre, self.socio.apellido, self.monto_disponible, self.tasa)
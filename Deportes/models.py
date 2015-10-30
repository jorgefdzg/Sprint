from django.db import models
# prueba de pull
# Create your models here.


class Deporte(models.Deporte):
    """docstring for deporte"""
    dpr_info = models.CharField(max_length="30")


class Amigos(models.Amigos):
    """docstring for Amigos"""
    usr_id1 = models.IntegerField(null=False, blank=True)
    usr_id2 = models.IntegerField(null=False, blank=True)


class Actividad(object):
    """docstring for Actividad"""
    clb_id = models.IntegerField(null=False, blank=True)
    usr_id = models.IntegerField(null=False, blank=True)
    act_info = models.CharField(max_length="500")


class DeporteUsuario(object):
    """docstring for Deporte-Usuario"""
    dpr_id = models.IntegerField(null=False, blank=True)
    usr_id = models.IntegerField(null=False, blank=True)

from django.db import models
# prueba de pull
# Create your models here.


class Deporte(models.Model):
    """docstring for deporte"""
    dpr_info = models.CharField(max_length="30")


class Amigos(models.Model):
    """docstring for Amigos"""
    usr_id1 = models.IntegerField(null=True, blank=False)
    usr_id2 = models.IntegerField(null=True, blank=False)


class Actividad(models.Model):
    """docstring for Actividad"""
    clb_id = models.IntegerField(null=True, blank=False)
    usr_id = models.IntegerField(null=True, blank=False)
    act_info = models.CharField(max_length="500")


class DeporteUsuario(models.Model):
    """docstring for Deporte-Usuario"""
    dpr_id = models.IntegerField(null=True, blank=False)
    usr_id = models.IntegerField(null=True, blank=False)

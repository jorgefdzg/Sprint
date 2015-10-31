from django.db import models
# prueba de pull
# Create your models here.


class Deporte(models.Model):
    """docstring for deporte"""
    dpr_info = models.CharField(max_length="30")


class Usuario(models.Model):
    """docstring for Usuario"""
    usr_nom = models.CharField(max_length="60")
    usr_cor = models.EmailField(max_length="60")
    usr_usu = models.CharField(max_length="30")
    usr_pas = models.CharField(max_length="40")
    usr_edad = models.IntegerField(null=True, blank=False)


class Direccion(models.Model):
    """docstring for Direccion"""
    drc_estado = models.CharField(max_length="20")
    drc_municipio = models.CharField(max_length="20")
    drc_colonia = models.CharField(max_length="30")
    drc_codigo = models.IntegerField(null=True, blank=False)
    drc_calle = models.CharField(max_length="20")
    drc_num = models.IntegerField(null=True, blank=False)


class Amigos(models.Model):
    """docstring for Amigos"""
    usr_id1 = models.ForeignKey(Usuario)
    usr_id2 = models.ForeignKey(Usuario)


class Club(models.Model):
    """docstring for Club"""
    clb_nom = models.CharField(max_length="60")
    clb_dir = models.ForeignKey(Direccion)


class Miembrosclub(models.Model):
    """docstring for Miembrosclub"""
    clb_id = models.ForeignKey(Club)
    usr_id = models.ForeignKey(Usuario)
    mcb_tipo = models.IntegerField(null=True, blank=False)


class Actividad(models.Model):
    """docstring for Actividad"""
    Act_clb_id = models.ForeignKey(Club)
    Act_usr_id = models.ForeignKey(Usuario)
    act_info = models.CharField(max_length="500")


class DeporteUsuario(models.Model):
    """docstring for Deporte-Usuario"""
    dpr_id = models.ForeignKey(Deporte)
    usr_id = models.ForeignKey(Usuario)

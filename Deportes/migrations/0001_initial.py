# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('act_info', models.CharField(max_length='500')),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('clb_nom', models.CharField(max_length='60')),
            ],
        ),
        migrations.CreateModel(
            name='Deporte',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('dpr_info', models.CharField(max_length='30')),
            ],
        ),
        migrations.CreateModel(
            name='DeporteUsuario',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('dpr_id', models.ForeignKey(to='Deportes.Deporte')),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('drc_estado', models.CharField(max_length='20')),
                ('drc_municipio', models.CharField(max_length='20')),
                ('drc_colonia', models.CharField(max_length='30')),
                ('drc_codigo', models.IntegerField(null=True)),
                ('drc_calle', models.CharField(max_length='20')),
                ('drc_num', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Miembrosclub',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('mcb_tipo', models.IntegerField(null=True)),
                ('clb_id', models.ForeignKey(to='Deportes.Club')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('usr_nom', models.CharField(max_length='60')),
                ('usr_cor', models.EmailField(max_length='60')),
                ('usr_usu', models.CharField(max_length='30')),
                ('usr_pas', models.CharField(max_length='40')),
                ('usr_edad', models.IntegerField(null=True)),
                ('usr_amg', models.ManyToManyField(to='Deportes.Usuario')),
            ],
        ),
        migrations.AddField(
            model_name='miembrosclub',
            name='usr_id',
            field=models.ForeignKey(to='Deportes.Usuario'),
        ),
        migrations.AddField(
            model_name='deporteusuario',
            name='usr_id',
            field=models.ForeignKey(to='Deportes.Usuario'),
        ),
        migrations.AddField(
            model_name='club',
            name='clb_dir',
            field=models.ForeignKey(to='Deportes.Direccion'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='Act_clb_id',
            field=models.ForeignKey(to='Deportes.Club'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='Act_usr_id',
            field=models.ForeignKey(to='Deportes.Usuario'),
        ),
    ]

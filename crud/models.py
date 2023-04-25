from asyncio.windows_events import NULL
from email.policy import default
from tabnanny import verbose
from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User
from django.forms import NullBooleanField, model_to_dict
import json

'''
Valores más frecuentes:
    - models.CharField
    - models.DateField
    - models.DateTimeField
    - models IntegerField
    - models.PositiveIntegerField
    - models.BooleanField
    - models.ImageField
    - models.FileField   (archivo)
'''

opcionesRV = [
    (0, 'Seleccione patología a filtrar'),
    (1 , 'TODOS LOS PACIENTES'),
    (2 , 'Diabetes'),
    (3, 'Hipertensión'),
    (4, 'Tabaquismo'),
    (5, 'Insuficiencia renal crónica'),
    (6, 'Hipercolesterolemia'),
    (7, 'Hipertrigliceridemia'),
    (8, 'Hiperlipemia mixta'),
    (9, 'Ex-fumador')
]


class Riesgo_Vascular(models.Model):
    riesgo = models.CharField(max_length=25,blank=True, unique=True,  null=True, verbose_name="Riesgo")
    codigo = models.CharField(max_length=25, blank=True, null=True, verbose_name="CIE-9")
    opcion = models.IntegerField(
        choices=opcionesRV,
        default = 1,
        verbose_name=''

    )
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Editado el', blank=True, null=True)

    usuario = models.ForeignKey(User, editable=False, verbose_name='Usuario', on_delete=models.CASCADE, blank=True, null=True)
    

    def __str__(self):
        
        return "%s" % (self.riesgo)

    class Meta:
        verbose_name = 'Riesgo_Vascular'
        verbose_name_plural = 'Riesgo_Vasculars'
        ordering = ['riesgo']



class Patologias(models.Model):
    patologia = models.CharField(max_length=100,blank=True, unique=True,  null=True, verbose_name="Patología")
    codigo = models.CharField(max_length=100, blank=True, null=True, verbose_name="CIE-9")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Editado el', blank=True, null=True)

    

    def __str__(self):
        
        return "%s" % (self.patologia)

    class Meta:
        verbose_name = 'Patologia'
        verbose_name_plural = 'Patologias'
        ordering = ['patologia']

class Marca(models.Model):
    marca = models.CharField(max_length=100,unique=True, blank=True, null=True, verbose_name="Marca")    
    laboratorio = models.CharField(max_length=100, blank = True, null = True, verbose_name="Laboratorio")
    visitador = models.CharField(max_length=100,unique=True, blank=True, null=True, verbose_name="Visitador")
    observaciones = models.TextField(max_length=100, blank=True, null=True, verbose_name="Observaciones")

    def __str__(self):
        
        return "%s" % (self.marca)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        ordering = ['marca']

  

class Presentaciones(models.Model):
    presentacion = models.CharField(max_length=200, blank = True, null = True, verbose_name="Presentación")
        
    def __str__(self):
        
        return "%s" % (self.presentacion)

    class Meta:
        verbose_name = 'Presentación'
        verbose_name_plural = 'Presentaciones'
        ordering = ['presentacion']   

class Farmacos(models.Model):
    farmaco = models.CharField(max_length=100, blank=False, null=False, unique=True, verbose_name="Fármaco", default="")
    grupo = models.CharField(max_length=100, blank=True, null=True, verbose_name="Grupo")
    subgrupo = models.CharField(max_length=100, blank=True, null=True, verbose_name="Subgrupo")
    marca = models.ManyToManyField(Marca, verbose_name='Marca', blank=True)    
    efecto = models.CharField(max_length=200, blank = True, null = True, verbose_name="Efecto")
    mecanismo_accion = models.TextField(max_length=250, blank=True, null=True, verbose_name="Mecanismo de acción")
    # presentaciones = models.ManyToManyField(Presentaciones, max_length=100, blank = True, verbose_name="Presentación")
    dosis_minima = models.FloatField(blank = True, null = True, default='0')
    dosis_FG_mayor_90 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Dosis mayor 90")
    dosis_60_89 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Dosis 60-89")
    dosis_45_59 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Dosis 45-59")
    dosis_30_44 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Dosis 30-44")
    dosis_15_29 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Dosis 15-29")
    dosis_FG_menor_15 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Dosis menor 15")
    dosis_maxima = models.FloatField(blank = True, null = True)
    intervalo_dosis = models.IntegerField(blank = True, null = True)   
    FG_quitar = models.IntegerField(blank = True, null = True)
    FG_no_iniciar = models.IntegerField(blank = True, default='0')
    FG_mayor_90  = models.CharField(max_length=100, blank=True, null=True, verbose_name="FG mayor de 90")
    FG_60_89  = models.CharField(max_length=100, blank=True, null=True, verbose_name="FG 60-89")
    FG_45_59  = models.CharField(max_length=100, blank=True, null=True, verbose_name="FG 45-59")
    FG_30_44  = models.CharField(max_length=100, blank=True, null=True, verbose_name="FG 30-44")
    FG_15_29  = models.CharField(max_length=100, blank=True, null=True, verbose_name="FG 15-29")
    FG_menor_15  = models.CharField(max_length=100, blank=True, null=True, verbose_name="FG menor de 15") 
    unidades = models.CharField(max_length=20, blank = True, null = True, verbose_name="Unidades")
    comentarios = models.TextField(max_length=1000, blank=True, null=True, verbose_name="Comentarios")
    ventajas = models.TextField(max_length=1000, blank=True, null=True, verbose_name="Ventajas")
    inconvenientes = models.TextField(max_length=1000, blank=True, null=True, verbose_name="Inconvenientes")

    created_at = models.DateTimeField(auto_now=True, verbose_name='Creado el', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Editado el', blank=True, null=True)

    

    def __str__(self):
        
        return "%s" % (self.farmaco)

    class Meta:
        verbose_name = 'Farmaco'
        verbose_name_plural = 'Farmacos'
        ordering = ['farmaco']


class Pacientes(models.Model):
   
    nuhsa = models.CharField(db_column='NUHSA', primary_key=True, max_length=12, verbose_name="NUHSA")  # Field name made lowercase.    
    nombre = models.CharField(max_length=100, null=True, blank=True,  verbose_name="Nombre")
    apellido1 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Primer Apellido")
    apellido2 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Segundo Apellido")
    fecha_nac = models.DateField(null=True, blank=True, verbose_name="Fecha nacimiento")
    descripcion = models.TextField(max_length=150, blank=True, null=True, verbose_name="Comentarios")
    patologia = models.ManyToManyField(Patologias, blank=True)
    riesgo_vascular = models.ManyToManyField(Riesgo_Vascular, blank=True)
    farmaco = models.ManyToManyField(Farmacos, blank=True)
    
    usuario = models.ForeignKey(User, verbose_name='Usuario', on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        fila = self.nuhsa + ' - ' + self.nombre + " " + self.apellido1 + "  " + self.apellido2
        # 
        return fila

    # def toJSON(self):
    #     item = model_to_dict(self, exclude['patologia', 'riesgo_vascular', 'farmaco'])        
    #     return item
    
    def edad(self):
        if self.fecha_nac:
            hoy = date.today()
            edad = hoy.year - self.fecha_nac.year - (
                    (hoy.month, hoy.day) < (self.fecha_nac.month, self.fecha_nac.day))
            return edad
        # Si no tiene fecha su edad es 0
        return 0

    
    class Meta:
        verbose_name = 'Pacientes'
        verbose_name_plural = 'Pacientes'
        ordering = ['apellido1','apellido2']

class SituacionClinicaPrincipal(models.Model):
    situacion = models.CharField(max_length=100, null=True, blank=True,  verbose_name="situacion")
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.situacion

    class Meta:
        verbose_name = 'Patología Principal'
        verbose_name_plural = 'Patologías Principales'
        ordering = ['situacion']

class SituacionClinicaSecundaria(models.Model):
    situacion = models.CharField(max_length=100, null=True, blank=True,  verbose_name="situacion")
    activo = models.BooleanField(default=True)    
    situacion_principal = models.ForeignKey(SituacionClinicaPrincipal, max_length=100, blank = True, null = True, on_delete=models.CASCADE, verbose_name="situacion")

    def __str__(self):
        return self.situacion
    class Meta:
        verbose_name = 'Patología Secundaria'
        verbose_name_plural = 'Patologías Secundarias'
        ordering = ['situacion']

class SituacionClinicaTerciaria(models.Model):
    situacion = models.CharField(max_length=100, null=True, blank=True,  verbose_name="situacion")
    activo = models.BooleanField(default=True)    
    situacion_secundaria = models.ForeignKey(SituacionClinicaSecundaria, max_length=100, blank = True, null = True, on_delete=models.CASCADE, verbose_name="situacion")
    def __str__(self):
        return self.situacion
    class Meta:
        verbose_name = 'Patología Terciaria'
        verbose_name_plural = 'Patologías Terciarias'
        ordering = ['situacion']


from import_export import resources
from import_export.admin import ImportExportModelAdmin

from django.contrib import admin

from .models import Pacientes, Riesgo_Vascular, Patologias, Farmacos, Marca, Presentaciones, SituacionClinicaPrincipal, SituacionClinicaSecundaria, SituacionClinicaTerciaria

class FarmacosResource(resources.ModelResource):
    # fields = (
    #     'farmaco',
    #     'grupo',
    #     'subgrupo',                    
    #     'efecto',
    #     'mecanismo_accion',                    
    #     'dosis_minima',
    #     'dosis_FG_mayor_90',
    #     'dosis_60_89',
    #     'dosis_45_59',
    #     'dosis_30_44',
    #     'dosis_15_29',
    #     'dosis_FG_menor_15',
    #     'dosis_maxima',
    #     'intervalo_dosis',
    #     'FG_quitar',
    #     'FG_no_iniciar',
    #     'FG_mayor_90',
    #     'FG_60_89',
    #     'FG_45_59',
    #     'FG_30_44',
    #     'FG_15_29',
    #     'FG_menor_15',
    #     'unidades',
    #     'comentarios',
    #     'ventajas',
    #     'inconvenientes',
    # )
    class Meta:
        model = Farmacos

class PacientesAdmin(admin.ModelAdmin):
    
    search_fields = ('nuhsa', 'nombre', 'apellido1', 'apellido2')
    list_filter = ('riesgo_vascular',)


class FarmacosAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = FarmacosResource
    # list_display = ('farmaco', 'grupo', 'subgrupo', 'marca', 'dosis_minima', 'dosis_maxima')
   
    


class PatologiasAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('patologia','codigo')
    



    
        

admin.site.register(Pacientes, PacientesAdmin)
admin.site.register(Riesgo_Vascular)
admin.site.register(Patologias, PatologiasAdmin)
admin.site.register(Farmacos)
admin.site.register(Marca)
admin.site.register(Presentaciones)
admin.site.register(SituacionClinicaPrincipal)
admin.site.register(SituacionClinicaSecundaria)
admin.site.register(SituacionClinicaTerciaria)

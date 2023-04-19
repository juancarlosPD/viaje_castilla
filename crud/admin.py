from django.contrib import admin


from .models import Pacientes, Riesgo_Vascular, Patologias, Farmacos, Marca, Presentaciones, SituacionClinicaPrincipal, SituacionClinicaSecundaria, SituacionClinicaTerciaria

class PacientesAdmin(admin.ModelAdmin):
    
    search_fields = ('nuhsa', 'nombre', 'apellido1', 'apellido2')
    list_filter = ('riesgo_vascular',)

class FarmacossAdmin(admin.ModelAdmin):
    
    search_fields = ('farmaco', 'grupo', 'subgrupo', 'marca', 'dosis_minima', 'dosis_maxima')
    list_filter = ('riesgo_vascular',)
    


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

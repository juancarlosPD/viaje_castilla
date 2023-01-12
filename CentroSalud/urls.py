from django.urls import path
from CentroSalud import views

urlpatterns = [
    path('inicioCentroSalud/', views.inicioCentroSalud, name='inicioCentroSalud'),
    path('acuerdoGestion/', views.acuerdoGestion, name='acuerdoGestion'),
    path('objetivos2022/', views.objetivos2022, name='objetivos2022'),
    path('vacunas/', views.vacunas, name='vacunas'),
    path('documentoVacunas/', views.documentoVacunas, name='documentoVacunas'),
    path('anafilaxiaVacunacionCOVID/', views.anafilaxiaVacunacionCOVID, name='anafilaxiaVacunacionCOVID'),
    path('vacunaHerpesZoster/', views.vacunaHerpesZoster, name='vacunaHerpesZoster'),
    path('vacunaHepatitisA/', views.vacunaHepatitisA, name='vacunaHepatitisA'),
    path('vacunaHepatitisAB/', views.vacunaHepatitisAB, name='vacunaHepatitisAB'),
    path('documentosImprimir/', views.documentosImprimir, name='documentosImprimir'),
    path('telefonos/', views.telefonos, name='telefonos'),
    path('tabaco/', views.tabaco, name='tabaco'),
    path('visados/', views.visados, name='visados'),
    path('farmacia/', views.farmacia, name='farmacia'),
    path('IT/', views.IT, name='IT'),
    path('unidadesEspecializadasIT/', views.unidadesEspecializadasIT, name='unidadesEspecializadasIT'),
    path('peticionAmbulancia/', views.peticionAmbulancia, name='peticionAmbulancia'),
    path('transporte_sanitario/', views.transporte_sanitario, name='transporte_sanitario'),
    path('telefonosDistrito/', views.telefonosDistrito, name='telefonosDistrito'),
    

   
   
    path('POE_CertificadoDefuncion/', views.POE_CertificadoDefuncion, name='POE_CertificadoDefuncion'),
    path('resumen_POE_Certificados_defuncion/', views.resumen_POE_Certificados_defuncion, name='resumen_POE_Certificados_defuncion'),
    path('anexo1CD/', views.anexo1CD, name='anexo1CD'),

    
    # -------------------------VARIOS--------------------------------------------------------------
    path('solicitudOxigenoterapia/', views.solicitudOxigenoterapia, name='solicitudOxigenoterapia'),
    path('manual_oximesa/', views.manual_oximesa, name='manual_oximesa'),
    path('desburocratizacion/', views.desburocratizacion, name='desburocratizacion'),
    path('proteccion_datos/', views.proteccion_datos, name='proteccion_datos'),
    path('viruela_mono/', views.viruela_mono, name='viruela_mono'),
    path('lesiones_cutaneas_vm/', views.lesiones_cutaneas_vm, name='lesiones_cutaneas_vm'),
    path('estudio_contactos_ITS/', views.estudio_contactos_ITS, name='estudio_contactos_ITS'),


    # -------------------------VISADOS--------------------------------------------------------------
    path('condicionesACO/', views.condicionesACO, name='condicionesACO'),
    path('informeACO/', views.informeACO, name='informeACO'),
    path('condicionesADO/', views.condicionesADO, name='condicionesADO'),
    path('informeADO/', views.informeADO, name='informeADO'),
    path('visadoDiagnosticoHospitalario/', views.visadoDiagnosticoHospitalario, name='visadoDiagnosticoHospitalario'),
    path('visadoOtros/', views.visadoOtros, name='visadoOtros'),
    path('visadoCiertasIndicaciones/', views.visadoCiertasIndicaciones, name='visadoCiertasIndicaciones'),
    path('visadoVacunas/', views.visadoVacunas, name='visadoVacunas'),
    path('visadoNutricionEnteral/', views.visadoNutricionEnteral, name='visadoNutricionEnteral'),
    path('hojaSolicitudVisadoNutricionEnteral/', views.hojaSolicitudVisadoNutricionEnteral, name='hojaSolicitudVisadoNutricionEnteral'),

]
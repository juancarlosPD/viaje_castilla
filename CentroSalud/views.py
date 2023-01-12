from django.shortcuts import render
from django.http import HttpResponse

def inicioCentroSalud(request):    
    return render(request, 'inicioCentroSalud.html')

def acuerdoGestion(request):    
    return render(request, 'acuerdoGestion.html')

def objetivos2022(request):    
    return render(request, 'objetivos2022.html')

def vacunas(request):    
    return render(request, 'vacunas.html')

def documentoVacunas(request):    
    return render(request, 'documentoVacunas.html')

def vacunaHerpesZoster(request):    
    return render(request, 'vacunaHerpesZoster.html')

def anafilaxiaVacunacionCOVID(request):    
    return render(request, 'anafilaxiaVacunacionCOVID.html')

def documentosImprimir(request):    
    return render(request, 'documentosImprimir.html')

def telefonos(request):    
    return render(request, 'telefonos.html')

def tabaco(request):    
    return render(request, 'tabaco.html')

def visados(request):    
    return render(request, 'visados.html')

def farmacia(request):    
    return render(request, 'farmacia.html')

def IT(request):    
    return render(request, 'IT.html')

def unidadesEspecializadasIT(request):    
    return render(request, 'unidadesEspecializadasIT.html')

def peticionAmbulancia(request):    
    return render(request, 'peticionAmbulancia.html')

def telefonosDistrito(request):    
    return render(request, 'telefonosDistrito.html')

def vacunaHepatitisA(request):    
    return render(request, 'vacunaHepatitisA.html')

def vacunaHepatitisAB(request):    
    return render(request, 'vacunaHepatitisAB.html')


# -----------------VARIOS----------------------------------
def POE_CertificadoDefuncion(request):    
    return render(request, 'POES/certificadoDefuncion.html')

def resumen_POE_Certificados_defuncion(request):    
    return render(request, 'POES/resumen_POE_Certificados_defuncion.html')

def anexo1CD(request):    
    return render(request, 'POES/anexo1CD.html')

def transporte_sanitario(request):    
    return render(request, 'POES/transporte_sanitario.html')


def solicitudOxigenoterapia(request):    
    return render(request, 'solicitudOxigenoterapia.html')

def manual_oximesa(request):    
    return render(request, 'manual_oximesa.html')

def desburocratizacion(request):    
    return render(request, 'desburocratizacion.html')

def proteccion_datos(request):    
    return render(request, 'proteccion_datos.html')

def viruela_mono(request):    
    return render(request, 'viruela_mono.html')

def lesiones_cutaneas_vm(request):    
    return render(request, 'lesiones_cutaneas_vm.html')

def estudio_contactos_ITS(request):    
    return render(request, 'estudio_contactos_ITS.html')

# ---------------------VISADOS-----------------------------

def condicionesACO(request):    
    return render(request, 'visados/condicionesACO.html')

def informeACO(request):    
    return render(request, 'visados/informeACO.html')

def condicionesADO(request):    
    return render(request, 'visados/condicionesADO.html')

def informeADO(request):    
    return render(request, 'visados/informeADO.html')

def visadoDiagnosticoHospitalario(request):    
    return render(request, 'visados/visadoDiagnosticoHospitalario.html')

def visadoOtros(request):    
    return render(request, 'visados/visadoOtros.html')

def visadoCiertasIndicaciones(request):    
    return render(request, 'visados/visadoCiertasIndicaciones.html')

def visadoVacunas(request):    
    return render(request, 'visados/visadoVacunas.html')

def visadoNutricionEnteral(request):    
    return render(request, 'visados/visadoNutricionEnteral.html')

def hojaSolicitudVisadoNutricionEnteral(request):    
    return render(request, 'visados/hojaSolicitudNutricionEnteral.html')
from django.shortcuts import render
from django.http import HttpResponse

def inicioEspecialidades(request):    
    return render(request, 'inicioEspecialidades.html')


def cardiologia(request):    
    return render(request, 'cardiologia.html')

def cirugia(request):    
    return render(request, 'cirugia.html')

def mujer(request):    
    return render(request, 'mujer.html')

def endocrino(request):    
    return render(request, 'endocrino.html')

def hematologia(request):    
    return render(request, 'hematologia.html')

def interna(request):    
    return render(request, 'interna.html')

def nefrologia(request):    
    return render(request, 'nefrologia.html')

def neurologia(request):    
    return render(request, 'neurologia.html')

def neumologia(request):    
    return render(request, 'neumologia.html')

def neurologia(request):    
    return render(request, 'neurologia.html')

def oftalmologia(request):    
    return render(request, 'oftalmologia.html')

def paliativos(request):    
    return render(request, 'paliativos.html')

def urologia(request):    
    return render(request, 'urologia.html')

def reumatologia(request):    
    return render(request, 'reumatologia.html')

def radiologia(request):    
    return render(request, 'radiologia.html')

# -----------------CARDIOLOGIA-----------------------------
def acuerdoCardiologia(request):    
    return render(request, 'cardiologia/acuerdoCardiologia.html')

# -----------------CIRUGIA-----------------------------
def cirugiaPlastica(request):    
    return render(request, 'cirugia/cirugiaPlastica.html')

# -----------------DIGESTIVO-----------------------------
def digestivo(request):    
    return render(request, 'digestivo.html')

def dispepsia(request):    
    return render(request, 'digestivo/dispepsia.html')

def dispepsiaTexto(request):    
    return render(request, 'digestivo/dispepsiaTexto.html')

def peticionEndoscopia(request):    
    return render(request, 'digestivo/peticionEndoscopia.html')

def testhp(request):    
    return render(request, 'digestivo/testhp.html')

def infeccionhp(request):    
    return render(request, 'digestivo/infeccionhp.html')

def colonoscopia(request):    
    return render(request, 'digestivo/colonoscopia.html')

def analitica(request):    
    return render(request, 'digestivo/analisis.html')

def acuerdoDigestivo(request):    
    return render(request, 'digestivo/acuerdoDigestivo.html')

# -----------------ENDOCRINOLOGIA-----------------------------

def vitaminaD(request):    
    return render(request, 'endocrino/VitaminaD.html')

def consensoVitaminaD(request):    
    return render(request, 'endocrino/consensoVitaminaD.html')

# -----------------HEMATOLOGIA-----------------------------

def esquemaSintrom(request):    
    return render(request, 'hematologia/esquemaSintrom.html')

def poeSintrom(request):    
    return render(request, 'hematologia/poeSintrom.html')

def consejosPaciente(request):    
    return render(request, 'hematologia/consejosPaciente.html')

def informacionPaciente(request):    
    return render(request, 'hematologia/informacionPaciente.html')

def valoracionEnfermeria(request):    
    return render(request, 'hematologia/valoracionEnfermeria.html')




# -----------------M. INTERNA-----------------------------

def acuerdoInterna(request):    
    return render(request, 'interna/acuerdoInterna.html')

# -----------------NEUMOLOGIA-----------------------------

def acuerdoNeumologia(request):    
    return render(request, 'neumologia/acuerdoNeumologia.html')

def ttoCefaleas(request):    
    return render(request, 'neurologia/ttoCefaleas.html')

# -----------------NEUMOLOGIA-----------------------------

def acuerdoNeurologia(request):    
    return render(request, 'neurologia/acuerdoNeurologia.html')

# -----------------LABORATORIO-----------------------------

def laboratorio(request):    
    return render(request, 'laboratorio.html')

def analisisClinicos(request):    
    return render(request, 'laboratorio/analisisClinicos.html')

def perfilesAnaliticos(request):    
    return render(request, 'laboratorio/perfilesAnaliticos.html')

def estudiosGeneticos(request):    
    return render(request, 'laboratorio/estudiosGeneticos.html')

# -----------------LOCOMOTOR-----------------------------
def locomotor(request):    
    return render(request, 'locomotor.html')

def higienePostural(request):    
    return render(request, 'locomotor/higienePostural.html')

def cadera(request):    
    return render(request, 'locomotor/cadera.html')

def cervicalgia(request):    
    return render(request, 'locomotor/cervicalgia.html')

def codo(request):    
    return render(request, 'locomotor/codo.html')   

def dorsalgia(request):    
    return render(request, 'locomotor/dorsalgia.html')

def hombro(request):    
    return render(request, 'locomotor/hombro.html')

def lumbalgia(request):    
    return render(request, 'locomotor/lumbalgia.html')

def mano(request):    
    return render(request, 'locomotor/mano.html')

def osteoporosis(request):    
    return render(request, 'locomotor/osteoporosis.html')

def pie(request):    
    return render(request, 'locomotor/pie.html')

def plantillas(request):    
    return render(request, 'locomotor/plantillas.html')

def rodilla(request):    
    return render(request, 'locomotor/rodilla.html')

#----------------------EJERCICIOS--------------------------------------------------
def ejerciciosCervicalgia(request):    
    return render(request, 'locomotor/ejercicios/ejerciciosCervicalgia.html')

def ejerciciosLumbalgia(request):    
    return render(request, 'locomotor/ejercicios/ejerciciosLumbalgia.html')

def ejerciciosEspondilitis(request):    
    return render(request, 'locomotor/ejercicios/ejerciciosEspondilitis.html')  

def ejerciciosRodilla(request):    
    return render(request, 'locomotor/ejercicios/ejerciciosRodilla.html')

#----------------------EXPLORACIÓN--------------------------------------------------

def exploracionCadera(request):    
    return render(request, 'locomotor/exploracion/exploracionCadera.html')

def exploracionCervicalgia(request):    
    return render(request, 'locomotor/exploracion/exploracionCervicalgia.html')

def exploracionCodo(request):    
    return render(request, 'locomotor/exploracion/exploracionCodo.html')

def exploracionHombro(request):    
    return render(request, 'locomotor/exploracion/exploracionHombro.html')

def exploracionLumbalgia(request):    
    return render(request, 'locomotor/exploracion/exploracionLumbalgia.html')

def exploracionMano(request):    
    return render(request, 'locomotor/exploracion/exploracionMano.html')

def exploracionPie(request):    
    return render(request, 'locomotor/exploracion/exploracionPie.html')

def exploracionRodilla(request):    
    return render(request, 'locomotor/exploracion/exploracionRodilla.html')

# ----------------------MUJER--------------------------------------------------------------
def mamas(request):    
    return render(request, 'mujer/mamas.html')

def ovario(request):    
    return render(request, 'mujer/ovario.html')

def utero(request):    
    return render(request, 'mujer/utero.html')

def cuelloUtero(request):    
    return render(request, 'mujer/cuelloUtero.html')

def vagina(request):    
    return render(request, 'mujer/vagina.html')

def planificacion(request):    
    return render(request, 'mujer/planificacion.html')

def implanon(request):    
    return render(request, 'mujer/implanon.html')

def embarazo(request):    
    return render(request, 'mujer/embarazo.html')

def menopausia(request):    
    return render(request, 'mujer/menopausia.html')

def reproduccionAsistida(request):    
    return render(request, 'mujer/reproduccionAsistida.html')

# ----------------------NEFROLOGÍA--------------------------------------------------------------
def ajusteFarmacosIRC(request):    
    return render(request, 'nefrologia/ajusteFarmacosIRC.html')

def consensoIRC(request):    
    return render(request, 'nefrologia/consensoIRC.html')

def manejoPatologiasIRC(request):    
    return render(request, 'nefrologia/manejoPatologiasIRC.html')

# ----------------------PALIATIVOS--------------------------------------------------------------
def guiaSedacionPaliativa(request):    
    return render(request, 'paliativos/guiaSedacionPaliativa.html')

# ----------------------REUMATOLOGIA--------------------------------------------------------------
def osteoporosisGascon(request):    
    return render(request, 'reumatologia/osteoporosisGascon.html')

def prevencionOsteoporosis(request):    
    return render(request, 'reumatologia/prevencionOsteoporosis.html')

def dietaCalcio(request):    
    return render(request, 'reumatologia/dietaCalcio.html')

def consenso_vitD(request):    
    return render(request, 'reumatologia/consenso_vitD.html')

# ----------------------RADIOLOGIA--------------------------------------------------------------
def solicitudEcografia(request):    
    return render(request, 'radiologia/solicitudEcografia.html')


# -----------------UROLOGIA-----------------------------

def acuerdoUrologia(request):    
    return render(request, 'urologia/acuerdoUrologia.html')

def recomendacionesITU(request):    
    return render(request, 'urologia/recomendacionesITU.html')

def recomendacionesUrolitiasis(request):    
    return render(request, 'urologia/recomendacionesUrolitiasis.html')



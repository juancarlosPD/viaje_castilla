from django.shortcuts import render
from django.http import HttpResponse
from .models import Rey

def inicioPersonal(request):    
    return render(request, 'inicioPersonal.html')

def inicioFilosofia(request):    
    return render(request, 'filosofia/inicioFilosofia.html')

def inicioHistoria(request):    
    return render(request, 'inicioHistoria.html')

def reyesEspagna(request):    
    return render(request, 'espagna/reyesEspagna.html')
# -------------------HISTORIA-----------------------------------------
    
def inicioEspagna(request):    
    return render(request, 'espagna/inicioEspagna.html')

def inicioInglaterra(request):    
    return render(request, 'inglaterra/inicioInglaterra.html')

# ----------------------------SIGLO XVI--------------------------

    # ----------------------------ESPAÑA--------------------------
def sigloXVI(request):    
    return render(request, 'espagna/sigloXVI/inicioSigloXVI.html')

def sucesionIsabelCatolica(request):    
    return render(request, 'espagna/sigloXVI/sucesionIsabelCatolica.html')

def carlosI(request):    
    return render(request, 'espagna/sigloXVI/carlosI.html')

def felipeII(request):    
    return render(request, 'espagna/sigloXVI/felipeII.html')  

def sigloXIX(request):    
    return render(request, 'espagna/sigloXIX/sigloXIX.html')

def restauracion(request):    
    return render(request, 'espagna/sigloXIX/restauracion.html')

    # ----------------------------INGLATERRA--------------------------
def sigloXVIIng(request):    
    return render(request, 'inglaterra/sigloXVI/inicioXVIIng.html')

def enriqueVIII(request):    
    return render(request, 'inglaterra/sigloXVI/enriqueVIII.html')

# ----------------------------SIGLO XI--------------------------
def sigloXI(request):    
    return render(request, 'espagna/sigloXI/inicioSigloXI.html')

def alfonsoVI(request):    
    return render(request, 'espagna/sigloXI/alfonsoVI.html')

# ----------------------------SIGLO XII--------------------------
def sigloXII(request):    
    return render(request, 'espagna/sigloXII/inicioSigloXII.html')

def urraca(request):    
    return render(request, 'espagna/sigloXII/urraca.html')

def alfonsoVII(request):    
    return render(request, 'espagna/sigloXII/alfonsoVII.html')

def alfonsoVIII(request):    
    return render(request, 'espagna/sigloXII/alfonsoVIII.html')


# ----------------------------SIGLO XVII--------------------------
def sigloXVII(request):    
    return render(request, 'espagna/sigloXVII/inicioSigloXVII.html')

def resumenSigloXVII(request):    
    return render(request, 'espagna/sigloXVII/resumenSigloXVII.html')

def felipeIII(request):    
    return render(request, 'espagna/sigloXVII/felipeIII.html')

def felipeIV(request):    
    return render(request, 'espagna/sigloXVII/felipeIV.html')

def carlosII(request):    
    return render(request, 'espagna/sigloXVII/carlosII.html')

# ----------------------------SIGLO XVIII--------------------------
def sigloXVIII(request):    
    return render(request, 'espagna/sigloXVIII/sigloXVIII.html')

def ilustracion(request):    
    return render(request, 'espagna/sigloXVIII/ilustracion.html')

# ----------------------------SIGLO XIX--------------------------
def carlosIV(request):    
    return render(request, 'espagna/sigloXIX/carlosIV.html')

def independencia(request):    
    return render(request, 'espagna/sigloXIX/guerraIndependencia.html')

def monarquiaAbsoluta(request):    
    return render(request, 'espagna/sigloXIX/monarquiaAbsoluta.html')

def regencias(request):    
    return render(request, 'espagna/sigloXIX/regencias.html')

def isabelII(request):    
    return render(request, 'espagna/sigloXIX/isabelII.html')

def sexenioDemocratico(request):    
    return render(request, 'espagna/sigloXIX/sexenioDemocratico.html')

def movimientoObrero(request):    
    return render(request, 'espagna/sigloXIX/movimientoObrero.html')

def guerrasCarlistas(request):    
    return render(request, 'espagna/sigloXIX/guerrasCarlistas.html')

def guerraCuba(request):    
    return render(request, 'espagna/sigloXIX/guerraCuba.html')

def restauracion(request):    
    return render(request, 'espagna/sigloXIX/restauracion.html')

def constituciones(request):    
    return render(request, 'espagna/sigloXIX/constituciones.html')

def partidosPoliticos(request):    
    return render(request, 'espagna/sigloXIX/partidosPoliticos.html')

def monedas1868(request):    
    return render(request, 'espagna/sigloXIX/monedas1868.html')

def escritoresxix(request):    
    return render(request, 'espagna/sigloXIX/escritores.html')

# ----------------------------SIGLO XX--------------------------
def sigloXX(request):    
    return render(request, 'espagna/sigloXX/sigloXX.html')

def alfonsoXIII(request):    
    return render(request, 'espagna/sigloXX/alfonsoXIII.html')

def primoRivera(request):    
    return render(request, 'espagna/sigloXX/primoRivera.html')

def segundaRepublica(request):    
    return render(request, 'espagna/sigloXX/segundaRepublica.html')

#----------------------------------- GUERRA CIVIL

def guerraCivil(request):    
    return render(request, 'espagna/sigloXX/guerraCivil.html')

def calvo_sotelo(request):    
    return render(request, 'espagna/sigloXX/guerraCivil/calvo_sotelo.html')

def golpe_17_julio_1936(request):    
    return render(request, 'espagna/sigloXX/guerraCivil/golpe_17_julio_1936.html')

def golpe_18_julio(request):    
    return render(request, 'espagna/sigloXX/guerraCivil/golpe_18_julio.html')

def verano_36(request):    
    return render(request, 'espagna/sigloXX/guerraCivil/verano_36.html')

def retaguardia(request):    
    return render(request, 'espagna/sigloXX/guerraCivil/retaguardias.html')




def franco(request):    
    return render(request, 'espagna/sigloXX/franco.html')

def transicion(request):    
    return render(request, 'espagna/sigloXX/transicion.html')


   

# -------------------FILOSOFIA-----------------------------------------
def intuicion(request):    
    return render(request, 'filosofia/intuicion.html')

def metodoFilosofia(request):    
    return render(request, 'filosofia/metodoFilosofia.html')


def reyes_cards(request):
    reyes = Rey.objects.all()
    return render(request, "espagna/reyesEspagna.html", {"reyes": reyes})

def reyes_timeline(request):
    reyes = Rey.objects.all()
    return render(request, "espagna/reyes_timeline.html", {"reyes": reyes})

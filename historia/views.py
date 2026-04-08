from django.shortcuts import render
from django.http import HttpResponse
from .models import Rey

def inicioPersonal(request):    
    return render(request, 'inicioPersonal.html')

def inicioFilosofia(request):    
    return render(request, 'filosofia/inicioFilosofia.html')

def inicioHistoria(request):    
    return render(request, 'inicioHistoria.html')

def inicioClasica(request):    
    return render(request, 'inicioClasica.html')

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

def linea_tiempo_alfonso_XIII(request):    
    return render(request, 'espagna/sigloXX/linea_tiempo_alfonso_XIII.html')

def linea_tiempo_segunda_republica(request):    
    return render(request, 'espagna/sigloXX/linea_tiempo_segunda_republica.html')

def primoRivera(request):    
    return render(request, 'espagna/sigloXX/primoRivera.html')

def segundaRepublica(request):    
    return render(request, 'espagna/sigloXX/segundaRepublica.html')

# def presidentesXX(request):    
#     return render(request, 'espagna/sigloXX/presidentesXX.html')

def presidentesXX(request):
    presidentes = [
        {
            "orden": 1,
            "nombre": "Antonio Cánovas del Castillo",
            "apodo": "",
            "periodo": "1875–1881, 1884–1885, 1890–1892, 1895–1897",
            "etapa": "Restauración",
            "partido": "Partido Liberal-Conservador",
            "imagen": "images/sigloXX/presidentes/canovas.jpg",
            "resumen": "Principal arquitecto de la Restauración borbónica y del sistema político del turnismo."
        },
        {
            "orden": 2,
            "nombre": "Práxedes Mateo Sagasta",
            "apodo": "",
            "periodo": "1881–1883, 1885–1890, 1892–1895, 1897–1899, 1901–1902",
            "etapa": "Restauración",
            "partido": "Partido Liberal",
            "imagen": "images/sigloXX/presidentes/sagasta.png",
            "resumen": "Gran líder liberal de la Restauración y alternante habitual con Cánovas."
        },
        {
            "orden": 3,
            "nombre": "Antonio Maura",
            "apodo": "",
            "periodo": "1903–1904, 1907–1909, 1918, 1919, 1921–1922",
            "etapa": "Restauración",
            "partido": "Partido Conservador",
            "imagen": "images/sigloXX/presidentes/maura.png",
            "resumen": "Uno de los políticos más influyentes del reinado de Alfonso XIII."
        },
        {
            "orden": 4,
            "nombre": "José Canalejas",
            "apodo": "",
            "periodo": "1910–1912",
            "etapa": "Restauración",
            "partido": "Partido Liberal",
            "imagen": "images/sigloXX/presidentes/canalejas.png",
            "resumen": "Impulsó reformas modernizadoras hasta su asesinato en 1912."
        },
        {
            "orden": 5,
            "nombre": "Eduardo Dato",
            "apodo": "",
            "periodo": "1913–1915, 1917, 1920–1921",
            "etapa": "Restauración",
            "partido": "Partido Conservador",
            "imagen": "images/sigloXX/presidentes/dato.png",
            "resumen": "Figura clave del conservadurismo, asesinado en 1921."
        },
        {
            "orden": 6,
            "nombre": "Conde de Romanones",
            "apodo": "",
            "periodo": "1912–1913, 1915–1917, 1918, 1931",
            "etapa": "Restauración / Transición a la República",
            "partido": "Partido Liberal",
            "imagen": "images/sigloXX/presidentes/romanones1.png",
            "resumen": "Político muy presente en los últimos años de la monarquía de Alfonso XIII."
        },
        {
            "orden": 7,
            "nombre": "Miguel Primo de Rivera",
            "apodo": "",
            "periodo": "1923–1930",
            "etapa": "Dictadura de Primo de Rivera",
            "partido": "Directorio militar",
            "imagen": "images/sigloXX/presidentes/primo.png",
            "resumen": "Gobernó como jefe del Gobierno durante la dictadura iniciada en 1923."
        },
        {
            "orden": 8,
            "nombre": "Dámaso Berenguer",
            "apodo": "",
            "periodo": "1930–1931",
            "etapa": "Dictablanda",
            "partido": "Gobierno de transición",
            "imagen": "images/sigloXX/presidentes/berenguer.png",
            "resumen": "Intentó retornar a la normalidad constitucional tras Primo de Rivera."
        },
        {
            "orden": 9,
            "nombre": "Juan Bautista Aznar",
            "apodo": "",
            "periodo": "1931",
            "etapa": "Final de la Monarquía",
            "partido": "Gobierno monárquico",
            "imagen": "images/sigloXX/presidentes/juan_aznar.png",
            "resumen": "Último presidente del Gobierno de Alfonso XIII antes de la Segunda República."
        },
        {
            "orden": 10,
            "nombre": "Niceto Alcalá-Zamora",
            "apodo": "",
            "periodo": "1931",
            "etapa": "Segunda República",
            "partido": "Gobierno provisional",
            "imagen": "images/sigloXX/presidentes/alcala_zamora.png",
            "resumen": "Presidió el Gobierno provisional antes de pasar a la Presidencia de la República."
        },
        {
            "orden": 11,
            "nombre": "Manuel Azaña",
            "apodo": "",
            "periodo": "1931–1933",
            "etapa": "Segunda República",
            "partido": "Izquierda republicana",
            "imagen": "images/sigloXX/presidentes/azaña.jpg",
            "resumen": "Figura esencial del reformismo republicano."
        },
        {
            "orden": 12,
            "nombre": "Alejandro Lerroux",
            "apodo": "",
            "periodo": "1933–1934, 1934–1935",
            "etapa": "Segunda República",
            "partido": "Partido Radical",
            "imagen": "images/sigloXX/presidentes/lerroux.png",
            "resumen": "Presidente del Gobierno durante el bienio radical-cedista."
        },
        {
            "orden": 13,
            "nombre": "Diego Martínez Barrio",
            "apodo": "",
            "periodo": "1933, 1936",
            "etapa": "Segunda República",
            "partido": "Republicano",
            "imagen": "images/sigloXX/presidentes/martinez_barrios.png",
            "resumen": "Tuvo mandatos muy breves en momentos de gran inestabilidad."
        },
        {
            "orden": 14,
            "nombre": "Santiago Casares Quiroga",
            "apodo": "",
            "periodo": "1936",
            "etapa": "Segunda República",
            "partido": "Izquierda republicana",
            "imagen": "images/sigloXX/presidentes/casares_quiroga.png",
            "resumen": "Presidente del Gobierno en vísperas del golpe de julio de 1936."
        },
        {
            "orden": 15,
            "nombre": "José Giral",
            "apodo": "",
            "periodo": "1936",
            "etapa": "Segunda República",
            "partido": "Republicano",
            "imagen": "images/sigloXX/presidentes/giral.png",
            "resumen": "Asumió el Gobierno tras el inicio de la Guerra Civil."
        },
        {
            "orden": 16,
            "nombre": "Francisco Largo Caballero",
            "apodo": "",
            "periodo": "1936–1937",
            "etapa": "Segunda República",
            "partido": "PSOE",
            "imagen": "images/sigloXX/presidentes/largo_caballero.jpg",
            "resumen": "Dirigió el Gobierno republicano en plena guerra."
        },
        {
            "orden": 17,
            "nombre": "Juan Negrín",
            "apodo": "",
            "periodo": "1937–1939",
            "etapa": "Segunda República",
            "partido": "PSOE",
            "imagen": "images/sigloXX/presidentes/negrin.jpg",
            "resumen": "Último presidente del Gobierno de la Segunda República durante la guerra."
        },
        {
            "orden": 18,
            "nombre": "Francisco Franco",
            "apodo": "",
            "periodo": "1938–1973",
            "etapa": "Dictadura franquista",
            "partido": "Régimen franquista",
            "imagen": "images/sigloXX/presidentes/franco.png",
            "resumen": "Jefe del Estado y del Gobierno durante la dictadura."
        },
        {
            "orden": 19,
            "nombre": "Luis Carrero Blanco",
            "apodo": "",
            "periodo": "1973",
            "etapa": "Dictadura franquista",
            "partido": "Régimen franquista",
            "imagen": "images/sigloXX/presidentes/carrero_blanco.png",
            "resumen": "Nombrado presidente del Gobierno por Franco; fue asesinado en 1973."
        },
        {
            "orden": 20,
            "nombre": "Carlos Arias Navarro",
            "apodo": "",
            "periodo": "1973–1976",
            "etapa": "Final del franquismo / inicio de la Transición",
            "partido": "Régimen franquista",
            "imagen": "images/sigloXX/presidentes/arias_navarro.png",
            "resumen": "Último presidente del franquismo y primero de la monarquía de Juan Carlos I."
        },
        {
            "orden": 21,
            "nombre": "Adolfo Suárez",
            "apodo": "",
            "periodo": "1976–1981",
            "etapa": "Transición democrática",
            "partido": "UCD",
            "imagen": "images/sigloXX/presidentes/suarez.png",
            "resumen": "Figura clave de la Transición y de la Constitución de 1978."
        },
        {
            "orden": 22,
            "nombre": "Leopoldo Calvo-Sotelo",
            "apodo": "",
            "periodo": "1981–1982",
            "etapa": "Transición / democracia consolidada",
            "partido": "UCD",
            "imagen": "images/sigloXX/presidentes/calvo_sotelo.jpg",
            "resumen": "Presidió el Gobierno tras el 23-F y durante la entrada en la OTAN."
        },
        {
            "orden": 23,
            "nombre": "Felipe González",
            "apodo": "",
            "periodo": "1982–1996",
            "etapa": "Democracia",
            "partido": "PSOE",
            "imagen": "images/sigloXX/presidentes/felipe_gonzalez.jpg",
            "resumen": "Gobernó durante la modernización institucional y económica de España."
        },
        {
            "orden": 24,
            "nombre": "José María Aznar",
            "apodo": "",
            "periodo": "1996–2004",
            "etapa": "Democracia",
            "partido": "PP",
            "imagen": "img/presidentes/aznar.jpg",
            "resumen": "Presidió el Gobierno en años de crecimiento económico y mayoría absoluta."
        },
        {
            "orden": 25,
            "nombre": "José Luis Rodríguez Zapatero",
            "apodo": "",
            "periodo": "2004–2011",
            "etapa": "Democracia",
            "partido": "PSOE",
            "imagen": "img/presidentes/zapatero.jpg",
            "resumen": "Impulsó importantes reformas sociales y gobernó durante la crisis económica."
        },
        {
            "orden": 26,
            "nombre": "Mariano Rajoy",
            "apodo": "",
            "periodo": "2011–2018",
            "etapa": "Democracia",
            "partido": "PP",
            "imagen": "img/presidentes/rajoy.jpg",
            "resumen": "Presidió el Gobierno durante la recuperación económica y la crisis catalana."
        },
        {
            "orden": 27,
            "nombre": "Pedro Sánchez",
            "apodo": "",
            "periodo": "2018–actualidad",
            "etapa": "Democracia",
            "partido": "PSOE",
            "imagen": "img/presidentes/pedro_sanchez.jpg",
            "resumen": "Presidente del Gobierno desde la moción de censura de 2018."
        },
    ]

    contexto = {
        "titulo": "Línea temporal de presidentes del Gobierno",
        "subtitulo": "De Cánovas del Castillo a la actualidad",
        "presidentes": presidentes,
    }
    
    return render(request, 'espagna/sigloXX/presidentesXX.html', contexto)

#----------------------------------- GUERRA CIVIL

def guerraCivil(request):    
    return render(request, 'espagna/sigloXX/guerraCivil.html')

def golpe_estado(request):    
    return render(request, 'espagna/sigloXX/guerraCivil/golpe_estado.html')

def hacia_madrid(request):    
    return render(request, 'espagna/sigloXX/guerraCivil/hacia_madrid.html')

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

def generales_franquistas(request):    
    return render(request, 'espagna/sigloXX/guerraCivil/generales_franquistas.html')

def generales_republicanos(request):    
    return render(request, 'espagna/sigloXX/guerraCivil/generales_republicanos.html')

def galeria(request):    
    return render(request, 'espagna/sigloXX/guerraCivil/galeria.html')

def gobierno(request):    
    return render(request, 'espagna/sigloXX/guerraCivil/gobierno.html')

def mapas(request):    
    return render(request, 'espagna/sigloXX/guerraCivil/mapas.html')

def ejercito_africa(request):    
    return render(request, 'espagna/sigloXX/guerraCivil/ejercito_africa.html')

def apoyo_exterior(request):    
    return render(request, 'espagna/sigloXX/guerraCivil/apoyo_exterior.html')

def andalucia_extremadura(request):    
    return render(request, 'espagna/sigloXX/guerraCivil/andalucia_extremadura.html')





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

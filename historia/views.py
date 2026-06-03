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

def romanico(request):    
    return render(request, 'espagna/temas/romanico.html')

def edad_media(request):    
    return render(request, 'espagna/edad_media.html')

# ----------------------------EDAD MEDIA--------------------------

def reinos_cristianos(request):    
    return render(request, 'espagna/edad_media/reinos_cristianos.html')

def reino_asturias(request):    
    return render(request, 'espagna/edad_media/reinos_cristianos/reino_asturias.html')

def reyes_asturias(request):    
    return render(request, 'espagna/edad_media/reinos_cristianos/reyes_asturias.html')

def reino_leon(request):    
    return render(request, 'espagna/edad_media/reinos_cristianos/reino_leon.html')

def reyes_leon(request):    
    return render(request, 'espagna/edad_media/reinos_cristianos/reyes_leon.html')

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

def maria_cristina_hasburgo(request):    
    return render(request, 'espagna/sigloXIX/maria_cristina_hasburgo.html')

def cultura_pensamiento(request):    
    return render(request, 'espagna/sigloXIX/cultura_pensamiento.html')

# ----------------------------SIGLO XX--------------------------
def sigloXX(request):    
    return render(request, 'espagna/sigloXX/sigloXX.html')

def alfonsoXIII(request):    
    return render(request, 'espagna/sigloXX/alfonsoXIII_responsive.html')

def linea_tiempo_alfonso_XIII(request):    
    return render(request, 'espagna/sigloXX/linea_tiempo_alfonso_XIII.html')

def linea_tiempo_segunda_republica(request):    
    return render(request, 'espagna/sigloXX/linea_tiempo_segunda_republica.html')

def primoRivera(request):    
    return render(request, 'espagna/sigloXX/primoRivera.html')

def segundaRepublica(request):    
    return render(request, 'espagna/sigloXX/segundaRepublica.html')

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

def siglo_plata(request):
    generaciones = [
        {
            "titulo": "Generación del 98", 
            "caracteristicas": [
                "Preocupación por España",
                "Regeneracionismo",
                "Visión crítica y pesimista",
                "Lenguaje sobrio y antiretórico",
                "Castilla como símbolo",                
            ],           
            "escritores": [
                {
                    "orden": 1,
                    "nombre": "Miguel de Unamuno y Jugo",
                    "generacion": "Generación 98",
                    "periodo": "Bilbao, 1864–Salamanca, 1936",            
                    "facetas": "Filósofo, novelista, poeta, ensayista, dramaturgo.",
                    "imagen": "images/sigloXX/escritores/unamuno.jpg",
                    "obra": "Del sentimiento trágico de la vida (1913), Niebla (1914), San Manuel Bueno, mártir (1931).",
                    "resumen": "Comprometido con la regeneración de España, fue crítico tanto del monarquismo como de la dictadura de Miguel Primo de Rivera, lo que le llevó al destierro en Fuerteventura y luego al exilio en Francia (1924–1930). Tras la proclamación de la Segunda República Española, regresó triunfal a Salamanca. Durante la Guerra Civil Española, se distanció de ambos bandos. El célebre enfrentamiento con el general José Millán Astray en el paraninfo de la universidad simboliza su defensa de la razón y la humanidad: “Vencer no es convencer”. Murió confinado en su casa. Su legado perdura como símbolo del pensamiento crítico y la conciencia moral de España."
                },
                {
                    "orden": 2,
                    "nombre": "Pío Baroja y Nessi",
                    "generacion": "Generación 98",
                    "periodo": "San Sebastian,1872 - Madrid, 1956",            
                    "facetas": "Médico. Novelista.",
                    "imagen": "images/sigloXX/escritores/baroja.avif",
                    "obra": "Trilogía “La lucha por la vida” (La busca, Mala hierba, Aurora roja): retrato de los barrios bajos madrileños. Trilogía “La raza” (La dama errante, La ciudad de la niebla, El árbol de la ciencia): exploración existencial y autobiográfica. Serie “Memorias de un hombre de acción” (22 volúmenes): epopeya histórica inspirada en su antepasado Eugenio de Aviraneta.",
                    "resumen": "Considerado el novelista por excelencia del 98, Baroja influyó en autores como Camilo José Cela y Ernest Hemingway. Su entierro en el Cementerio Civil de Madrid simbolizó su espíritu libre y anticlerical. Aún hoy, su visión lúcida y desencantada de España mantiene plena vigencia."
                },
                {
                    "orden": 3,
                    "nombre": "José Martínez Ruiz (Azorín)",
                    "generacion": "Generación 98",
                    "periodo": "Monóvar, 1873–Madrid, 1967",            
                    "facetas": "Novelista, ensayista, crítico literario y político español.",
                    "imagen": "images/sigloXX/escritores/azorin.webp",
                    "obra": "La voluntad, Antonio Azorín, Las confesiones de un pequeño filósofo, La ruta de Don Quijote, Castilla.",
                    "resumen": "Participó activamente en la vida pública durante la Restauración, siendo diputado y subsecretario de Instrucción Pública. Su evolución ideológica lo llevó del anarquismo inicial al conservadurismo. Tras la Guerra Civil española residió un tiempo en París, regresando a España en 1949. Fue miembro de la Real Academia Española desde 1924 y recibió la Gran Cruz de Alfonso X el Sabio. Su influencia perdura como símbolo de introspección, precisión estilística y amor por la cultura y el paisaje españoles."
                },
                {
                    "orden": 4,
                    "nombre": "Antonio Machado",
                    "generacion": "Generación 98",                    
                    "periodo": "Sevilla,1875 - Collioure,1939",            
                    "facetas": "Poeta, dramaturgo y pensador español.",
                    "imagen": "images/sigloXX/escritores/machado.jpg",
                    "obra": "Soledades, Campos de Castilla, Juan de Mairena.",
                    "resumen": "Partidario de la Segunda República, permaneció fiel al ideal democrático durante la Guerra Civil Española. En 1939 huyó con su familia a Francia, donde murió poco después en el exilio. Su tumba en Collioure simboliza la dignidad intelectual del exiliado. Hoy es considerado uno de los grandes poetas en lengua española, modelo de claridad ética y de emoción contenida."
                },
                {
                    "orden": 5,
                    "nombre": "Ramiro de Maeztu",
                    "generacion": "Generación 98",                    
                    "periodo": "Vitoria, 1875 - Aravaca, 1936",            
                    "facetas": "Periodista, ensayista, diplomático y pensador político español.",
                    "imagen": "images/sigloXX/escritores/maeztu.png",
                    "obra": "Hacia otra España (1899). La crisis del humanismo (1919). Don Quijote, Don Juan y La Celestina (1926). Defensa de la Hispanidad (1934).",
                    "resumen": "Escritor y ensayista del 98, pasó de ideas socialistas y regeneracionistas a convertirse en un ideólogo del nacional‑catolicismo. Defendió la Hispanidad y fue embajador con Primo de Rivera. Fusilado al inicio de la Guerra Civil."
                },
            ]
        },

        {
            "titulo": "Generación del 14 (Novecentismo)",
            "caracteristicas": [
                "Intelectualismo y racionalismo frente al 98",
                "Europeísmo como proyecto cultural",
                "Predominio del ensayo",
                "Arte puro y depurado"
            ],
            "escritores": [
                {
                    "orden": 1,
                    "nombre": "José Ortega y Gasset",
                    "periodo": "Madrid, 1883–1955",
                    "facetas": "Filósofo, ensayista y humanista",
                    "imagen": "images/sigloXX/escritores/ortega.jpg",
                    "obra": "Meditaciones del Quijote (1914), España invertebrada (1921), La rebelión de las masas (1930)",
                    "resumen": "Filósofo y ensayista clave del siglo XX, Ortega y Gasset fue el principal impulsor de la modernización intelectual de España. Su pensamiento, centrado en el perspectivismo —según el cual toda realidad se comprende desde una visión individual— y el raciovitalismo, que integra razón y vida como ejes inseparables, ofreció una interpretación dinámica del ser humano y la sociedad. Analizó con lucidez la crisis de su tiempo, especialmente en obras como 'La rebelión de las masas', y ejerció una influencia decisiva en generaciones posteriores de pensadores y en la proyección europea de la cultura española."
                },
                {
                    "orden": 2,
                    "nombre": "Gregorio Marañón",
                    "periodo": "Madrid, 1887–1960",
                    "facetas": "Médico, científico, historiador y ensayista",
                    "imagen": "images/sigloXX/escritores/marañon.png",
                    "obra": "Ensayo biológico sobre Enrique IV de Castilla y su tiempo (1930)",
                    "resumen": "Marañón combinó la ciencia con una profunda reflexión humanista. Defendió que “no hay enfermedades sino enfermos”, y abordó temas como la sexualidad, la ética profesional y la psicología médica. Fue comentarista de Sigmund Freud y estableció puentes entre psicoanálisis y biología. Como ensayista y biógrafo, interpretó figuras históricas —como Tiberio, Luis Vives o El Greco— desde un enfoque médico y moral. De ideología liberal, participó en la Agrupación al Servicio de la República junto a José Ortega y Gasset y Ramón Pérez de Ayala. Fue diputado en las Cortes de 1931. Durante la Guerra Civil se exilió en París (1936–1943) y regresó tras la contienda, retomando su labor científica y docente."
                },
                {
                    "orden": 3,
                    "nombre": "Ramón Pérez de Ayala",
                    "periodo": "Oviedo, 1887–Madrid,1960",
                    "facetas": "Escritor, periodista, diplomático y político español,",
                    "imagen": "images/sigloXX/escritores/perez_ayala.jpg",
                    "obra": "Troteras y danzaderas, Belarmino y Apolonio y Tigre Juan.",
                    "resumen": "Destacó como novelista y ensayista, con obras que combinan intelectualismo, ironía y análisis moral. Fue también embajador en el Reino Unido durante la Segunda República y miembro de la Real Academia Española."
                },
                {
                    "orden": 4,
                    "nombre": "Eugenio D'Ors",
                    "periodo": "Madrid, 1887–1960",
                    "facetas": "Escritor, filósofo, periodista y crítico de arte español",
                    "imagen": "images/sigloXX/escritores/dors.jpg",
                    "obra": "Fue autor del célebre Glosari, una columna diaria de crítica cultural ",
                    "resumen": "Figura central del Novecentismo que defendía el orden, la inteligencia y la modernización cultural frente al individualismo modernista. Ocupó cargos relevantes como director de Instrucción Pública en Cataluña y más tarde director general de Bellas Artes. También fue miembro de la Real Academia Española.  "
                }
            ]
        },

        {
            "titulo": "Generación del 27",
            "caracteristicas": [
                "Fusión tradición y vanguardia",
                "Influencia del surrealismo",
                "Uso intensivo metáfora",
                "Formación intelectual",
                "Espíritu de grupo",                
            ], 
            "escritores": [
                {
                    "orden": 1,
                    "nombre": "Federico García Lorca",
                    "periodo": "Fuente Vaqueros, 1898–Granada, 1936",
                    "facetas": "Poeta, dramaturgo y director teatral español",
                    "imagen": "images/sigloXX/escritores/lorca.jpg",
                    "obra": "Romancero gitano, Poeta en Nueva York, Bodas de sangre, Yerma, La casa de Bernarda Alba.",
                    "resumen": "Alcanzó reconocimiento internacional por su capacidad para unir tradición andaluza, simbolismo y vanguardias como el surrealismo. Fue también codirector del grupo teatral universitario La Barraca, con el que llevó el teatro clásico por toda España durante la Segunda República. Al inicio de la Guerra Civil, fue detenido y fusilado por las fuerzas sublevadas en 1936; su cuerpo nunca ha sido encontrado."
                },
                {
                    "orden": 2,
                    "nombre": "Rafael Alberti",
                    "periodo": "Puerto de Sta María 1902–1999",
                    "facetas": "Poeta, dramaturgo y pintor español",
                    "imagen": "images/sigloXX/escritores/alberti.jpg",
                    "obra": "Marinero en tierra, Sobre los ángeles, El poeta en la calle",
                    "resumen": "Comenzó su trayectoria artística como pintor, pero tras la muerte de su padre se volcó en la poesía, publicando Marinero en tierra (1924), obra con la que obtuvo el Premio Nacional de Literatura. Su obra evolucionó desde la poesía popular y andaluza hacia el neogongorismo, el surrealismo (Sobre los ángeles) y más tarde hacia una poesía política y comprometida, especialmente tras su afiliación al Partido Comunista de España. Durante la Guerra Civil, apoyó activamente a la República y, tras su derrota, vivió un largo exilio en Argentina, Italia y Francia. Regresó a España en 1977, ya en democracia, donde recibió importantes reconocimientos como el Premio Cervantes. "
                },
                {
                    "orden": 3,
                    "nombre": "Luís Cernuda",
                    "periodo": "Sevilla, 1902-Ciudad de México, 1963",
                    "facetas": "Escritor, traductor, profesor universitario, crítico literario y poeta",
                    "imagen": "images/sigloXX/escritores/cernuda.jpg",
                    "obra": "'La realidad y el deseo', un volumen que reúne toda su producción poética y que refleja su evolución desde la poesía pura y el simbolismo hasta un tono más íntimo, directo y autobiográfico.",
                    "resumen": "Su obra se caracteriza por un tono nostálgico, melancólico y neorromántico, con una profunda reflexión sobre la identidad, el deseo, la soledad y la libertad. Vivió marcado por su homosexualidad en una sociedad represiva, lo que influyó decisivamente en su poesía y en su sentimiento de desarraigo. Tras la Guerra Civil, se exilió en Inglaterra, Estados Unidos y México, donde continuó escribiendo."
                },
                {
                    "orden": 4,
                    "nombre": "Vicente Aleixandre",
                    "periodo": "Sevilla, 1898–Madrid, 1984",
                    "facetas": "Poeta",
                    "imagen": "images/sigloXX/escritores/aleixandre.jpg",
                    "obra": "Espadas como labios (1932). Sombra del paraíso (1944). Historia del corazón (1954). Poemas de la consumación (1968)",
                    "resumen": "Su obra evolucionó desde un surrealismo poético —visible en libros como Espadas como labios o Pasión de la tierra— hacia un lirismo más humanista y cósmico, centrado en temas como el amor, la fraternidad, la naturaleza y la condición humana. Marcado por una salud frágil desde joven, pasó largos periodos de convalecencia que influyeron en su introspección poética. Fue miembro de la Real Academia Española desde 1950 y se convirtió en un referente y maestro para generaciones posteriores de poetas. Recibió el <strong>Premio Nobel de Literatura</strong> en 1977."
                },
                {
                    "orden": 5,
                    "nombre": "Santiago Ramón y Cajal",
                    "periodo": "Navarra, Madrid, 1934",
                    "facetas": "Médico, histólogo y científico español",
                    "imagen": "images/sigloXX/escritores/cajal.jpg",
                    "obra": "Recuerdos de mi vida. Textura del sistema nervioso del hombre y de los vertebrados. Reglas y consejos sobre investigación científica",
                    "resumen": "Considerado el padre de la neurociencia moderna. Su trabajo revolucionó el conocimiento del sistema nervioso al demostrar que está formado por células individuales, las neuronas. Desarrolló técnicas de tinción propias que permitieron observar con precisión la estructura del tejido nervioso y describió regiones como la retina y múltiples áreas del sistema nervioso central. Fue profesor en las universidades de Valencia, Barcelona y Madrid, y dirigió instituciones científicas clave como el Instituto Nacional de Higiene y el Instituto Cajal. En 1906 recibió el <strong>Premio Nobel de Medicina</strong>, compartido con Camillo Golgi, por sus descubrimientos sobre la estructura del sistema nervioso. "
                },
                {
                    "orden": 6,
                    "nombre": "Severo Ochoa",
                    "periodo": "Luarca, 1905–Madrid, 1993",
                    "facetas": "Médico, bioquímico y científico español",
                    "imagen": "images/sigloXX/escritores/ochoa.jpg",
                    "obra": "Severo Ochoa: De la bioquímica a la biología molecular. Palabra de científico. Química de los ácidos nucleicos",
                    "resumen": "Nacionalizado estadounidense en 1956, y uno de los grandes pioneros de la biología molecular del siglo XX. Es mundialmente conocido por sus descubrimientos sobre la síntesis del ARN, lo que le valió el <strong>Premio Nobel de Fisiología o Medicina</strong> en 1959"
                },
                {
                    "orden": 7,
                    "nombre": "Pablo Picaso",
                    "periodo": "Fuente Vaqueros, 1898–Granada, 1936",
                    "facetas": "Poeta y dramaturgo",
                    "imagen": "images/sigloXX/escritores/picasso.jpg",
                    "obra": "Romancero gitano...",
                    "resumen": "Máximo exponente del 27..."
                },
                {
                    "orden": 8,
                    "nombre": "Salvador Dalí",
                    "periodo": "Fuente Vaqueros, 1898–Granada, 1936",
                    "facetas": "Poeta y dramaturgo",
                    "imagen": "images/sigloXX/escritores/dali.jpg",
                    "obra": "Romancero gitano...",
                    "resumen": "Máximo exponente del 27..."
                },
                {
                    "orden": 9,
                    "nombre": "Luís Buñuel",
                    "periodo": "Fuente Vaqueros, 1898–Granada, 1936",
                    "facetas": "Poeta y dramaturgo",
                    "imagen": "images/sigloXX/escritores/buñuel.webp",
                    "obra": "Romancero gitano...",
                    "resumen": "Máximo exponente del 27..."
                }
            ]
        }
    ]

    return render(request, 'espagna/sigloXX/siglo_plata.html', {
        "generaciones": generaciones
    })
    

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

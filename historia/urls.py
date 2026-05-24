from django.urls import path
from historia import views

urlpatterns = [
    path('inicioPersonal/', views.inicioPersonal, name='inicioPersonal'),
    path('inicioFilosofia/', views.inicioFilosofia, name='inicioFilosofia'),
    path('inicioHistoria/', views.inicioHistoria, name='inicioHistoria'),
    path('inicioClasica/', views.inicioClasica, name='inicioClasica'),
    path('reyesEspagna/', views.reyesEspagna, name='reyesEspagna'),

    # ----------------------------HISTORIA--------------------------
    path('inicioEspagna/', views.inicioEspagna, name='inicioEspagna'),
    path('inicioInglaterra/', views.inicioInglaterra, name='inicioInglaterra'),
    path('romanico/', views.romanico, name='romanico'),
    path('edad_media/', views.edad_media, name='edad_media'),

    # ----------------------------EDAD MEDIA--------------------------
    path('reinos_cristiano/', views.reinos_cristianos, name='reinos_cristianos'),
    path('reino_asturias/', views.reino_asturias, name='reino_asturias'),
    path('reino_leon/', views.reino_leon, name='reino_leon'),
    path('reyes_asturias/', views.reyes_asturias, name='reyes_asturias'),
    path('reyes_leon/', views.reyes_leon, name='reyes_leon'),

     # ----------------------------SIGLO XI--------------------------
    path('sigloXI/', views.sigloXI, name='sigloXI'),
    path('alfonsoVI/', views.alfonsoVI, name='alfonsoVI'),

    # ----------------------------SIGLO XII--------------------------
    path('sigloXII/', views.sigloXII, name='sigloXII'),
    path('urraca/', views.urraca, name='urraca'),
    path('alfonsoVII/', views.alfonsoVII, name='alfonsoVII'),
    path('alfonsoVIII/', views.alfonsoVIII, name='alfonsoVIII'),

    # ----------------------------SIGLO XVI--------------------------
    path('sigloXVI/', views.sigloXVI, name='sigloXVI'),
    path('sucesionIsabelCatolica/', views.sucesionIsabelCatolica, name='sucesionIsabelCatolica'),
    path('carlosI/', views.carlosI, name='carlosI'),
    path('felipeII/', views.felipeII, name='felipeII'),

    path('sigloXVIIng/', views.sigloXVIIng, name='sigloXVIIng'),
    path('enriqueVIII/', views.enriqueVIII, name='enriqueVIII'),

    # ----------------------------SIGLO XVII--------------------------
    path('sigloXVII/', views.sigloXVII, name='sigloXVII'),
    path('resumenSigloXVII/', views.resumenSigloXVII, name='resumenSigloXVII'),
    path('felipeIII/', views.felipeIII, name='felipeIII'),
    path('felipeIV/', views.felipeIV, name='felipeIV'),
    path('carlosII/', views.carlosII, name='carlosII'),

    # ----------------------------SIGLO XVIII--------------------------
    path('sigloXVIII/', views.sigloXVIII, name='sigloXVIII'),
    path('ilustracion/', views.ilustracion, name='ilustracion'),

    # ----------------------------SIGLO XIX--------------------------
    path('sigloXIX/', views.sigloXIX, name='sigloXIX'),
    path('carlosIV/', views.carlosIV, name='carlosIV'),
    path('independencia/', views.independencia, name='independencia'),
    path('monarquiaAbsoluta/', views.monarquiaAbsoluta, name='monarquiaAbsoluta'),
    path('regencias/', views.regencias, name='regencias'),
    path('isabelII/', views.isabelII, name='isabelII'),
    path('sexenioDemocratico/', views.sexenioDemocratico, name='sexenioDemocratico'),
    path('movimientoObrero/', views.movimientoObrero, name='movimientoObrero'),
    path('movimientoObrero/', views.movimientoObrero, name='movimientoObrero'),
    path('guerrasCarlistas/', views.guerrasCarlistas, name='guerrasCarlistas'),
    path('guerraCuba/', views.guerraCuba, name='guerraCuba'),
    path('restauracion/', views.restauracion, name='restauracion'),
    path('constituciones/', views.constituciones, name='constituciones'),
    path('partidosPoliticos/', views.partidosPoliticos, name='partidosPoliticos'),
    path('monedas1868/', views.monedas1868, name='monedas1868'),
    path('escritoresxix/', views.escritoresxix, name='escritoresxix'),
    path('maria_cristina_hasburgo/', views.maria_cristina_hasburgo, name='maria_cristina_hasburgo'),

    # ----------------------------SIGLO XX--------------------------
    path('sigloXX/', views.sigloXX, name='sigloXX'),
    path('siglo_plata/', views.siglo_plata, name='siglo_plata'),
    path('alfonsoXIII/', views.alfonsoXIII, name='alfonsoXIII'),
    path('primoRivera/', views.primoRivera, name='primoRivera'),
    path('segundaRepublica/', views.segundaRepublica, name='segundaRepublica'),
    path('guerraCivil/', views.guerraCivil, name='guerraCivil'),
    path('franco/', views.franco, name='franco'),
    path('transicion/', views.transicion, name='transicion'),
    path('presidentesXX/', views.presidentesXX, name='presidentesXX'),
    path('linea_tiempo_alfonso_XIII/', views.linea_tiempo_alfonso_XIII, name='linea_tiempo_alfonso_XIII'),
    path('linea_tiempo_segunda_republica/', views.linea_tiempo_segunda_republica, name='linea_tiempo_segunda_republica'),

    # ------------------------GUERRA CIVIL
    path('sigloXX/guerra_civil/golpe_estado', views.golpe_estado, name='golpe_estado'),
    path('sigloXX/guerra_civil/calvo_sotelo', views.calvo_sotelo, name='calvo_sotelo'),
    path('sigloXX/guerra_civil/golpe_julio_36', views.golpe_17_julio_1936, name='golpe_17_julio_1936'),
    path('sigloXX/guerra_civil/hacia_madrid', views.hacia_madrid, name='hacia_madrid'),
    path('sigloXX/guerra_civil/18_julio', views.golpe_18_julio, name='golpe_18_julio'),
    path('sigloXX/guerra_civil/verano_36', views.verano_36, name='verano_36'),
    path('sigloXX/guerra_civil/retaguardia', views.retaguardia, name='retaguardia'),
    path('sigloXX/guerra_civil/generales_franquistas', views.generales_franquistas, name='generales_franquistas'),
    path('sigloXX/guerra_civil/generales_republicanos', views.generales_republicanos, name='generales_republicanos'),
    path('sigloXX/guerra_civil/galeria', views.galeria, name='galeria'),
    path('sigloXX/guerra_civil/gobierno', views.gobierno, name='gobierno'),
    path('sigloXX/guerra_civil/mapas', views.mapas, name='mapas'),
    path('sigloXX/guerra_civil/ejercito_africa', views.ejercito_africa, name='ejercito_africa'),
    path('sigloXX/guerra_civil/apoyo_exterior', views.apoyo_exterior, name='apoyo_exterior'),
    path('sigloXX/guerra_civil/andalucia_extremadura', views.andalucia_extremadura, name='andalucia_extremadura'),

    # ----------------------------FILOSOFIA--------------------------
    path('metodoFilosofia/', views.metodoFilosofia, name='metodoFilosofia'),
    path('intuicion/', views.intuicion, name='intuicion'),

     # ----------------------------REYES ESPAÑA--------------------------
    path("reyes/", views.reyesEspagna, name="reyesEspagna"),
    path("reyes/timeline/", views.reyes_timeline, name="reyes_timeline"),
    
]


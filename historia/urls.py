from django.urls import path
from historia import views

urlpatterns = [
    path('inicioPersonal/', views.inicioPersonal, name='inicioPersonal'),
    path('inicioFilosofia/', views.inicioFilosofia, name='inicioFilosofia'),
    path('inicioHistoria/', views.inicioHistoria, name='inicioHistoria'),

    # ----------------------------HISTORIA--------------------------
    path('inicioEspagna/', views.inicioEspagna, name='inicioEspagna'),
    path('inicioInglaterra/', views.inicioInglaterra, name='inicioInglaterra'),

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

    # ----------------------------SIGLO XX--------------------------
    path('sigloXX/', views.sigloXX, name='sigloXX'),
    path('alfonsoXIII/', views.alfonsoXIII, name='alfonsoXIII'),
    path('primoRivera/', views.primoRivera, name='primoRivera'),
    path('segundaRepublica/', views.segundaRepublica, name='segundaRepublica'),
    path('guerraCivil/', views.guerraCivil, name='guerraCivil'),
    path('franco/', views.franco, name='franco'),
    path('transicion/', views.transicion, name='transicion'),

    # ----------------------------FILOSOFIA--------------------------
    path('metodoFilosofia/', views.metodoFilosofia, name='metodoFilosofia'),
    path('intuicion/', views.intuicion, name='intuicion'),
    
]


from django.urls import path
from diabetes import views
from diabetes.api import *

urlpatterns = [
    path('inicioDiabetes/', views.inicioDiabetes, name='inicioDiabetes'),
    path('ado/', views.ado, name='ado'),
    path('ttoAdo/', views.ttoAdo, name='ttoAdo'),
    path('ttoDMSAS/', views.ttoDMSAS, name='ttoDMSAS'),
    path('ttoSEMI/', views.ttoSEMI, name='ttoSEMI'),
    path('ayudasTto/', views.ayudasTto, name='ayudasTto'),
    path('insulinizacion/', views.insulinizacion, name='insulinizacion'),
    path('insulinas/', views.insulinas, name='insulinas'),
    
    # --------------------TRATAMIENTOS----------------------------------------------------------
    path('listadoTtos/', views.listadoTtos, name='listadoTtos'),
    path('tto1/', views.tto1, name='tto1'),
    path('tto2/', views.tto2, name='tto2'),    
    path('farmacosFG/', views.farmacosFG, name='farmacosFG'),
    path('autocomplete/', views.autocomplete, name='autocomplete'),
    path('retinografias/', views.retinografias, name='retinografias'),
    path('solicitudRetinografias/', views.solicitudRetinografias, name='solicitudRetinografias'),
    path('lecturaRetinografias/', views.lecturaRetinografias, name='lecturaRetinografias'),
    path('retinopatias/', views.retinopatias, name='retinopatias'),
    path('algoritmoredGDPS/', views.algoritmoredGDPS, name='algoritmoredGDPS'),
    path('insulinizacionSaedyn/', views.insulinizacionSaedyn, name='insulinizacionSaedyn'),
    path('insulinizacionGDPS/', views.insulinizacionGDPS, name='insulinizacionGDPS'),
    path('palomares/', views.palomares, name='palomares'),
    path('informeVisado/', views.informeVisado, name='informeVisado'),
    path('condicionesVisado/', views.condicionesVisado, name='condicionesVisado'),
    path('tablaFarmacosFG/', views.tablaFarmacosFG, name='tablaFarmacosFG'),
    
    # ------------------DISPOSITIVOS------------------------------------------------
    path('solostar/', views.solostar, name='solostar'),
    path('novopen/', views.novopen, name='novopen'),

    
    
] + [

    path('api/farmacos/', FarmacosApi.as_view(), name='api-farmacos'),
    path('api/situacionPrincipal/', SituacionPrincipalApi.as_view(), name='api-situacionPrincipal'),
    path('api/situacionSecundaria/', SituacionSecundariaApi.as_view(), name='api-situacionSecundaria'),
    path('api/situacionTerciaria/', SituacionTerciariaApi.as_view(), name='api-situacionTerciaria'),
]
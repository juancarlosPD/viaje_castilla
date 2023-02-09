from django.urls import path
from especialidades import views

urlpatterns = [
    path('inicioEspecialidades/', views.inicioEspecialidades, name='inicioEspecialidades'),

    # ------------------ESPECIALIDADES------------------------------------------------------------------
    path('cardiologia/', views.cardiologia, name='cardiologia'),
    path('cirugia/', views.cirugia, name='cirugia'),
    path('mujer/', views.mujer, name='mujer'),
    path('endocrino/', views.endocrino, name='endocrino'),
    path('hematologia/', views.hematologia, name='hematologia'),
    path('interna/', views.interna, name='interna'),
    path('nefrologia/', views.nefrologia, name='nefrologia'),
    path('neumologia/', views.neumologia, name='neumologia'),
    path('neurologia/', views.neurologia, name='neurologia'),
    path('oftalmologia/', views.oftalmologia, name='oftalmologia'),
    path('paliativos/', views.paliativos, name='paliativos'),
    path('urologia/', views.urologia, name='urologia'),
    path('reumatologia/', views.reumatologia, name='reumatologia'),
    path('radiologia/', views.radiologia, name='radiologia'),

    # ------------------CARDIOLOGÍA------------------------------------------------------------------
    path('acuerdoCardiologia/', views.acuerdoCardiologia, name='acuerdoCardiologia'),

    # ---------------------CIRUGIA---------------------------------------------------------------
    path('cirugiaPlastica/', views.cirugiaPlastica, name='cirugiaPlastica'),

    # ------------------DIGESTIVO------------------------------------------------------------------
    path('digestivo/', views.digestivo, name='digestivo'),
    path('acuerdoDigestivo/', views.acuerdoDigestivo, name='acuerdoDigestivo'),
    path('dispepsia/', views.dispepsia, name='dispepsia'),
    path('dispepsiaTexto/', views.dispepsiaTexto, name='dispepsiaTexto'),
    path('peticionEndoscopia/', views.peticionEndoscopia, name='peticionEndoscopia'),
    path('testhp/', views.testhp, name='testhp'),
    path('infeccionhp/', views.infeccionhp, name='infeccionhp'),
    path('colonoscopia/', views.colonoscopia, name='colonoscopia'),
    path('analitica/', views.analitica, name='analitica'),

    # ----------------------ENDOCRINOLOGÍA--------------------------------------------------------------
    path('vitaminaD/', views.vitaminaD, name='vitaminaD'),
    path('consensoVitaminaD/', views.consensoVitaminaD, name='consensoVitaminaD'),


    # ----------------------HEMATOLOGIA--------------------------------------------------------------
    
    path('esquemaSintrom/', views.esquemaSintrom, name='esquemaSintrom'),
    path('poeSintrom/', views.poeSintrom, name='poeSintrom'),
    path('consejosPaciente/', views.consejosPaciente, name='consejosPaciente'),
    path('informacionPaciente/', views.informacionPaciente, name='informacionPaciente'),
    path('valoracionEnfermeria/', views.valoracionEnfermeria, name='valoracionEnfermeria'),

    # ----------------------M. INTERNA--------------------------------------------------------------
    path('acuerdoInterna/', views.acuerdoInterna, name='acuerdoInterna'),

    # ----------------------NEUMOLOGIA-------------------------------------------------------------
    path('acuerdoNeumologia/', views.acuerdoNeumologia, name='acuerdoNeumologia'),

    # ----------------------NEUROLOGIA-------------------------------------------------------------
    path('acuerdoNeurologia/', views.acuerdoNeurologia, name='acuerdoNeurologia'),
    path('ttoCefaleas/', views.ttoCefaleas, name='ttoCefaleas'),

    # ----------------------LABORATORIO--------------------------------------------------------------
    path('laboratorio/', views.laboratorio, name='laboratorio'),
    path('analisisClinicos/', views.analisisClinicos, name='analisisClinicos'),
    path('perfilesAnaliticos/', views.perfilesAnaliticos, name='perfilesAnaliticos'),
    path('estudiosGeneticos/', views.estudiosGeneticos, name='estudiosGeneticos'),

    # -----------------------LOCOMOTOR-------------------------------------------------------------
    path('locomotor/', views.locomotor, name='locomotor'),
    path('higienePostural/', views.higienePostural, name='higienePostural'),
    path('cervicalgia/', views.cervicalgia, name='cervicalgia'),
    path('exploracionCervicalgia/', views.exploracionCervicalgia, name='exploracionCervicalgia'),
    path('ejerciciosCervicalgia/', views.ejerciciosCervicalgia, name='ejerciciosCervicalgia'),
    path('dorsalgia/', views.dorsalgia, name='dorsalgia'),
    path('lumbalgia/', views.lumbalgia, name='lumbalgia'),
    path('osteoporosis/', views.osteoporosis, name='osteoporosis'),
    path('exploracionLumbalgia/', views.exploracionLumbalgia, name='exploracionLumbalgia'),
    path('ejerciciosLumbalgia/', views.ejerciciosLumbalgia, name='ejerciciosLumbalgia'),
    path('ejerciciosEspondilitis/', views.ejerciciosEspondilitis, name='ejerciciosEspondilitis'),    
    path('hombro/', views.hombro, name='hombro'),
    path('exploracionHombro/', views.exploracionHombro, name='exploracionHombro'),
    path('codo/', views.codo, name='codo'),
    path('exploracionCodo/', views.exploracionCodo, name='exploracionCodo'),
    path('mano/', views.mano, name='mano'),
    path('exploracionMano/', views.exploracionMano, name='exploracionMano'),
    path('rodilla/', views.rodilla, name='rodilla'),
    path('ejerciciosRodilla/', views.ejerciciosRodilla, name='ejerciciosRodilla'),
    path('exploracionRodilla/', views.exploracionRodilla, name='exploracionRodilla'),
    path('cadera/', views.cadera, name='cadera'),
    path('exploracionCadera/', views.exploracionCadera, name='exploracionCadera'),
    path('pie/', views.pie, name='pie'),
    path('plantillas/', views.plantillas, name='plantillas'),
    path('exploracionPie/', views.exploracionPie, name='exploracionPie'),

    # ----------------------MUJER--------------------------------------------------------------
    path('mamas/', views.mamas, name='mamas'),    
    path('cuelloUtero/', views.cuelloUtero, name='cuelloUtero'),
    path('embarazo/', views.embarazo, name='embarazo'),
    path('implanon/', views.implanon, name='implanon'),
    path('menopausia/', views.menopausia, name='menopausia'),
    path('ovario/', views.ovario, name='ovario'),
    path('reproduccionAsistida/', views.reproduccionAsistida, name='reproduccionAsistida'),
    path('planificacion/', views.planificacion, name='planificacion'),
    path('utero/', views.utero, name='utero'),
    path('vagina/', views.vagina, name='vagina'),

     # ----------------------NEFROLOGÍA--------------------------------------------------------------
    path('ajusteFarmacosIRC/', views.ajusteFarmacosIRC, name='ajusteFarmacosIRC'),
    path('consensoIRC/', views.consensoIRC, name='consensoIRC'),
    path('manejoPatologiasIRC/', views.manejoPatologiasIRC, name='manejoPatologiasIRC'), 

    # ----------------------PALIATIVOS--------------------------------------------------------------
    path('guiaSedacionPaliativa/', views.guiaSedacionPaliativa, name='guiaSedacionPaliativa'),
    

    # ---------------------REUMATOLOGIA---------------------------------------------------------------
    path('osteoporosisGascon/', views.osteoporosisGascon, name='osteoporosisGascon'),
    path('prevencionOsteoporosis/', views.prevencionOsteoporosis, name='prevencionOsteoporosis'),
    path('dietaCalcio/', views.dietaCalcio, name='dietaCalcio'),
    path('consenso_vitD/', views.consenso_vitD, name='consenso_vitD'),
    
     # ---------------------RADIOLOGIA---------------------------------------------------------------
    path('solicitudEcografia/', views.solicitudEcografia, name='solicitudEcografia'),
    
    # ---------------------RADIOLOGIA---------------------------------------------------------------
    path('acuerdoUrologia/', views.acuerdoUrologia, name='acuerdoUrologia'),
    path('recomendacionesITU/', views.recomendacionesITU, name='recomendacionesITU'),
    path('recomendacionesUrolitiasis/', views.recomendacionesUrolitiasis, name='recomendacionesUrolitiasis'),
    
]
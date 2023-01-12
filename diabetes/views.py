from datetime import datetime
from pickle import FALSE, TRUE
from tkinter import ON
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
import re
from .models import Farmacos
from django.views.generic import View, TemplateView, ListView
from .modulos.FiltradoGlomerular import *




def autocomplete(request):
    if 'term' in request.GET:
        farmacos = Farmacos.objects.filter(farmaco__icontains=request.GET.get('term'))
        lista = list()
        for farmaco in farmacos:
            lista.append(farmaco.farmaco)
        return JsonResponse(lista, safe=False)
    return render(request, 'farmacosFG.html')



def farmacosFG(request):
    respuesta1 = ""
    respuestaNoComenzar = ""  
    respuestaNoContinuar = ""
    respuestaSegunFG = ""
    marca = ""
    comentarios = ""
    dosis =""
    
    FG = ""
    farmaco = "" 
      
    if request.method =='POST':
        farmacoInt = request.POST.get('farmaco', False)
        FG = request.POST.get('FG', False)
        farmaco = Farmacos.objects.get(farmaco=farmacoInt)
        comentarios = farmaco.comentarios

        if farmaco.subgrupo == 'arGLP1':             
            marca = farmaco.marca
        else:
            marca =""   
        
        if int(FG) > 90 or int(FG) == 90:
            respuestaSegunFG = farmaco.FG_mayor_90
            dosis = farmaco.dosis_FG_mayor_90
        elif int(FG) >59 and int(FG) < 90:
            respuestaSegunFG = farmaco.FG_60_89
            dosis = farmaco.dosis_60_89
        elif int(FG) >44 and int(FG) < 60:
            respuestaSegunFG = farmaco.FG_45_59
            dosis = farmaco.dosis_45_59
            if farmaco.farmaco == 'Alogliptina':
                if int(FG) <50:
                    dosis = "12,5 mg / 24 h"
                else:
                    dosis = farmaco.dosis_45_59
            
        elif int(FG) >29 and int(FG) < 45:
            respuestaSegunFG = farmaco.FG_30_44
            dosis = farmaco.dosis_30_44
        elif int(FG) >14 and int(FG) < 30:
            respuestaSegunFG = farmaco.FG_15_29
            dosis = farmaco.dosis_15_29
            if farmaco.farmaco == 'Dapagliflozina':
                if int(FG) <25:
                    dosis = "0"
                else:
                    dosis = farmaco.dosis_15_29

            if farmaco.farmaco == 'Acarbosa':
                if int(FG) <25:
                    dosis = "0"
                else:
                    dosis = farmaco.dosis_15_29
        elif int(FG) <15 :
            respuestaSegunFG = farmaco.FG_menor_15
            dosis = farmaco.dosis_FG_menor_15  
        
       
        if int(FG) < int(farmaco.FG_quitar) or int(FG) == int(farmaco.FG_quitar):
            respuesta1 = " EL PACIENTE NO PUEDE TOMAR ESTE FÁRMACO"
            respuestaNoComenzar = f"Se recomienda NO COMENZAR con el fámaco cuando el FG baja de {farmaco.FG_no_iniciar + 1}"            
            respuestaNoContinuar = f" Se recomienza NO CONTINUAR con el tratamiento cuando el FG baja de {farmaco.FG_quitar + 1} "
        else:
            respuesta1 = " EL PACIENTE PUEDE TOMAR ESTE FÁRMACO "
            respuestaNoComenzar = ""
            respuestaNoContinuar = ""    

    return render(request, 'farmacosFG.html', 
        {'respuesta1': respuesta1, 
        # 'respuestaNoComenzar': respuestaNoComenzar, 
        # 'respuestaNoContinuar': respuestaNoContinuar, 
        'respuestaSegunFG' :respuestaSegunFG, 
        'FG': FG, 
        'farmaco':farmaco,
        'marca': marca,
        'comentarios': comentarios,
        'dosis' : dosis})



def ayudasTto(request):    
        
    ados = Farmacos.objects.filter(grupo = "ADO")
    farmacos = Farmacos.objects.all()

    #------------------------------------------------------------------------------------------------------
    #------------------------Variables por defecto----------------------------------------------------------
    #------------------------------------------------------------------------------------------------------
    dir1=""
    dir2=""
    dir3=""
    dir4=""
    cabecera1=""
    comentario1 =""
    color1 = ""
    pre1=""
    pre2=""
    pre3=""
    pre4=""
    post1=""
    post2=""
    post3=""
    post4=""
    grupo1=""
    grupo2=""
    grupo3=""
    grupo4=""
    subgrupo1 =""
    subgrupo2 =""
    subgrupo3 =""
    farmaco1=""
    farmaco2=""
    farmaco3=""
    nuevoFarmaco1 = ""
    numeroFarmacosAdicionar =""
    bajaGlicada1 = ""
    nuevoFarmaco2 = ""
    nuevoFarmaco3 = ""
    ultimo1=""
    ultimo2=""
    ultimo3=""
    ultimo4=""
    noUsar=""        
    url="ayudasTto.html"

    # --------------------------------------------------------------------------------------------------------
        
    if request.method=='POST':

        #------------------------------------------------------------------------------------------------------
        #------------------------Color del FG----------------------------------------------------------
        #------------------------------------------------------------------------------------------------------

        def colorFG():
            
            FG = int(request.POST.get('FG'))

            if FG > 59:
                colorC = "#28B463"
                colorT = "white"

                colores = []

                colores.append(colorC)
                colores.append(colorT)

            elif FG > 44 and FG <60:
                colorC = "#FFFF00"
                colorT = "black"

                colores = []

                colores.append(colorC)
                colores.append(colorT)
            
            elif FG > 29 and FG <45:
                colorC = "#FFD700"
                colorT = "black"

                colores = []

                colores.append(colorC)
                colores.append(colorT)

            elif FG > 14 and FG <30:
                colorC = "#FF0000"
                colorT = "black"

                colores = []

                colores.append(colorC)
                colores.append(colorT)
            
            else:
                colorC = "#B22222"
                colorT = "white"

                colores = []

                colores.append(colorC)
                colores.append(colorT)


            return(colores)
        
        #------------------------------------------------------------------------------------------------------
        #------------------------1º- Que está tomando----------------------------------------------------------
        #------------------------------------------------------------------------------------------------------
        metformina = request.POST.get('metformina')  # Devuelve 'on' si está picado y None si no lo está
               
        def estaTomando():
            
            numeroFarmacosActual =0
            resultado={}
            farmaco1 = request.POST.get('farmaco1')
            farmaco2 = request.POST.get('farmaco2')
            farmaco3 = request.POST.get('farmaco3')
            
            if farmaco1 == "1" and farmaco2 == None and farmaco3 == None:
                farmaco1=""
                farmaco2=""
                farmaco3=""                
                numeroFarmacosActual =0
                resultado['numeroFarmacosActual'] = numeroFarmacosActual
                
            elif farmaco1 != "1" and farmaco2 == "2" and farmaco3 == None:                
                farmaco2=""
                farmaco3=""
                numeroFarmacosActual =1
                farmaco1 = Farmacos.objects.get(farmaco=farmaco1)
                subgrupo1 = farmaco1.subgrupo                
                resultado['farmaco1'] = farmaco1
                resultado['subgrupo1'] = subgrupo1
                resultado['numeroFarmacosActual'] = numeroFarmacosActual
            elif farmaco1 != "1" and farmaco2 != "2" and farmaco2 != None and farmaco3 == "3":                
                farmaco3=""
                numeroFarmacosActual =2
                farmaco1 = Farmacos.objects.get(farmaco=farmaco1)                    
                subgrupo1 = farmaco1.subgrupo
                resultado['farmaco1'] = farmaco1
                resultado['subgrupo1'] = subgrupo1
                farmaco2 = Farmacos.objects.get(farmaco=farmaco2)
                subgrupo2 = farmaco2.subgrupo
                resultado['farmaco2'] = farmaco2
                resultado['subgrupo2'] = subgrupo2
                resultado['numeroFarmacosActual'] = numeroFarmacosActual
            elif farmaco1 != "1" and farmaco2 != "2" and farmaco2 != None and farmaco3 != "3" and farmaco3 != None:
                numeroFarmacosActual =3
                farmaco1 = Farmacos.objects.get(farmaco=farmaco1)                    
                subgrupo1 = farmaco1.subgrupo
                resultado['farmaco1'] = farmaco1
                resultado['subgrupo1'] = subgrupo1
                farmaco2 = Farmacos.objects.get(farmaco=farmaco2)
                subgrupo2 = farmaco2.subgrupo
                resultado['farmaco2'] = farmaco2
                resultado['subgrupo2'] = subgrupo2
                farmaco3 = Farmacos.objects.get(farmaco=farmaco3)
                subgrupo3 = farmaco3.subgrupo
                resultado['farmaco3'] = farmaco3
                resultado['subgrupo3'] = subgrupo3
                resultado['numeroFarmacosActual'] = numeroFarmacosActual
            
            return(resultado)

                
        #------------------------------------------------------------------------------------------------------
        #-----------------------2º- Es necesario conocer-------------------------------------------------------
        #------------------------------------------------------------------------------------------------------
        
        def necesarioConocer():
            resultado = {}
            cetosis = request.POST.get('cetosis')  # Devuelve 'on' si está picado y None si no lo está
            FG = int(request.POST.get('FG'))        
            glicada = float((request.POST.get('glicada')).replace(',','.'))
            objetivoGlicada = float(request.POST.get('objetivoGlicada'))
            desvioGlicada = float(glicada-objetivoGlicada)

            resultado['cetosis'] = cetosis
            resultado['FG'] = FG
            resultado['glicada'] = glicada
            resultado['objetivoGlicada'] = objetivoGlicada
            resultado['desvioGlicada'] = round(desvioGlicada,1)

            return(resultado)

    
        #------------------------------------------------------------------------------------------------------
        #---------------------3º- Situación clínica----------------------------------------------------------------
        #------------------------------------------------------------------------------------------------------

        predominante = request.POST.get('predominante')
        secundaria = request.POST.get('secundaria')
        terciaria = request.POST.get('terciaria')       
        
               
        #------------------------------------------------------------------------------------------------------
        #------------------------------------------PROTOCOLO----------------------------------------------
        #------------------------------------------------------------------------------------------------------
        
        necesarioConocer = necesarioConocer()
        estaTomando = estaTomando()        

        # -------------Recogemos datos--------------------------------------------
        FG = necesarioConocer['FG']
        glicada = necesarioConocer['glicada']
        cetosis = necesarioConocer['cetosis']
        objetivoGlicada = necesarioConocer['objetivoGlicada']
        desvioGlicada = necesarioConocer['desvioGlicada']        
       
        colores = colorFG()
        colorC = colores[0]
        colorT = colores[1]        

        try:
            farmaco1 = estaTomando['farmaco1']
            subgrupo1 = estaTomando['subgrupo1']
            if FG < farmaco1.FG_quitar:
                    color1 = '#FF0000' 
        
        except KeyError:
            farmaco1 = farmaco1
            
        try:
            farmaco2 = estaTomando['farmaco2']
            subgrupo2 = estaTomando['subgrupo2']
            if FG < farmaco2.FG_quitar:
                    color2 = '#FF0000'  
        
        except KeyError:
            farmaco2 = farmaco2

        try:
            farmaco3 = estaTomando['farmaco3']
            subgrupo3 = estaTomando['subgrupo3']
            if FG < farmaco3.FG_quitar:
                    color3 = '#FF0000'  
        
        except KeyError:
            farmaco3 = farmaco3        
        
        # ------------------Creamos la función tratamiento y recogemos datos--------------------

        def tratamiento():
            nuevoFarmaco1 = ""
            dir1 = ""
            bajaGlicada1 = ""
            comentario1 = ""
            if cetosis == 'on':
                url = 'ttos/ttoCetosisSi.html'
            else:
                if predominante == "Alto riesgo CV / Muy alto riesgo CV":
                    if secundaria == "IMC ≥ 30":
                        if terciaria == "Prevención primaria":
                            if FG >=30:
                                nuevoFarmaco1 = Farmacos.objects.get(farmaco='Dulaglutida')
                                dir1='#aGLP1'
                                comentario1 = '. Reduce eventos CV mayores fundamentalmente por la prevención del ictus.'
                                bajaGlicada1= 'Baja glicada 1-1,5 %'
                                nuevoGrupo2 = 'iSGLT2'                                
                                url = 'tratamiento1.html'
                                noRecomendado = ""
                                contraindicado = "" 
                                # url = 'ttos/tto1.html'                                                           
                            elif FG >=15 and FG < 30:                                
                                url = 'ttos/tto2.html'                               
                            elif FG < 15:                                
                                url = 'ttos/tto3.html'                                                  
                        elif terciaria == "Prevención secundaria":
                            if FG >=30:                                
                                url = 'ttos/tto4.html'
                            elif FG >=15 and FG <30:
                                url = 'ttos/tto2.html'
                            elif FG < 15:
                                url = 'ttos/tto3.html'
                        elif terciaria == "Obesidad lo más importante":
                            if FG >=30:                                
                                url = 'ttos/tto5.html'
                            elif FG >=15 and FG <30:                                
                                url = 'ttos/tto6.html'
                            elif FG < 15:                              
                                url = 'ttos/tto3.html'
                        
                    elif secundaria == "IMC < 30":
                        if FG >=30:
                            if terciaria == "Prevención primaria":
                                url = 'ttos/tto7.html'
                            elif terciaria == "Prevención secundaria":
                                url = 'ttos/tto8.html'                           
                        elif FG >=15 and FG <30:                           
                            url = 'ttos/tto9.html'                            
                        elif FG<15:
                            url = 'ttos/tto3.html'
                elif predominante == "Insuficiencia cardíaca":
                    
                    if FG >=30:
                        if secundaria == "IMC ≥ 30":
                            if terciaria == "FE ≤ 40":
                                url = 'ttos/tto10.html'
                            elif terciaria == "FE > 40":
                                url = 'ttos/tto11.html'
                        elif secundaria == "IMC < 30":
                            if terciaria == "FE ≤ 40":
                                url = 'ttos/tto12.html'
                            elif terciaria == "FE > 40":
                                url = 'ttos/tto13.html'
                    elif FG >=15 and FG < 30:
                        if secundaria == "IMC ≥ 30":
                            url = 'ttos/tto14.html'
                        elif secundaria == "IMC < 30":
                            url = 'ttos/tto15.html'
                    elif FG < 15:
                        url = 'ttos/tto3.html'                             
                elif predominante == "Insuficiencia renal crónica":
                    if FG > 59:
                        url = "farmacosFG/fg_mayor_60.html"
                    elif FG > 44 and FG < 60:
                        url = "farmacosFG/fg_45_60.html"
                    elif FG > 29 and FG < 45:
                        url = "farmacosFG/fg_30_45.html"
                    elif FG > 14 and FG < 30:
                        url = "farmacosFG/fg_15_30.html"
                    elif FG < 15:
                        url = "farmacosFG/fg_menor_15.html"

                elif predominante == "Sobrepeso/Obesidad":
                    if secundaria == "IMC ≥ 30":
                        if FG >=30:                                
                            url = 'ttos/tto5.html'                            
                        elif FG >=15 and FG <30:                                
                            url = 'ttos/tto6.html'
                        elif FG < 15:                              
                            url = 'ttos/tto3.html'
                    elif secundaria == "IMC < 30":
                        if FG >=30:                                
                            url = 'ttos/tto7.html'                            
                        elif FG >=15 and FG <30:                                
                            url = 'ttos/tto15.html'
                        elif FG < 15:                              
                            url = 'ttos/tto3.html'
                elif predominante == "Fragilidad":
                    pass

            resultado = [url, nuevoFarmaco1, dir1, bajaGlicada1, comentario1]  
            return(resultado)
                        
        tratamiento = tratamiento()

        # -----------------------------------------------------------------------------------------
        # --------------------------APLICAMOS EL PROTOCOLO EN SÍ-----------------------------------
        # -----------------------------------------------------------------------------------------
                    
        if desvioGlicada < 0:
            numeroFarmacosAdicionar = 0
            comentario="Este paciente no necesita ajustes en su tratamiento."
            predominante=""
            secundaria=""
            terciaria=""
        elif desvioGlicada >0 and desvioGlicada <= 1:            
            numeroFarmacosAdicionar = 1
            url = tratamiento[0]
            nuevoFarmaco1 = tratamiento[1]
            dir1 = tratamiento[2]
            bajaGlicada1 = tratamiento[3]
            comentario1 = tratamiento[4]            
        elif desvioGlicada >1 and desvioGlicada <= 2:            
            numeroFarmacosAdicionar = 2
            comentario= "Se puede optar entre un aGLP1  de alta potencia o 2 fármacos"
            url = tratamiento[0]
        elif desvioGlicada>2 or glicada > 9:            
            if cetosis == 'on' :
                comentario="Se recomienda insulinizar a este paciente"
                url = 'ttos/ttoCetosisSi.html'
            elif cetosis == None:    
                url = 'ttos/ttoCetosisNo.html'
                comentario = "Se recomienda usar arGLP1 asociado a iSGLT2" 

        # return ayudasTto POST--------------------------

        return render(request, url,
                {
                    'farmaco1': farmaco1,
                    'farmaco2': farmaco2,
                    'farmaco3': farmaco3,
                    'nuevoFarmaco1': nuevoFarmaco1,
                    'FG': FG,
                    'glicada': glicada,
                    'objetivoGlicada': objetivoGlicada,
                    'desvioGlicada':desvioGlicada,
                    'bajaGlicada1' : bajaGlicada1,
                    'numeroFarmacosAdicionar' : numeroFarmacosAdicionar,                    
                    'cabecera1' : cabecera1,
                    'dir1' : dir1,
                    'dir2' : dir2,
                    'dir3' : dir3,
                    'dir4' : dir4,
                    'pre1' : pre1,
                    'pre2' : pre2,
                    'pre3' : pre3,
                    'pre4' : pre4,
                    'post1' : post1,
                    'post2' : post2,
                    'post3' : post3,
                    'post4' : post4,
                    'predominante': predominante,
                    'secundaria': secundaria,
                    'terciaria': terciaria,
                    'grupo1' : grupo1,
                    'grupo2' : grupo2,
                    'grupo3' : grupo3,
                    'grupo4' : grupo4,
                    'subgrupo1' : subgrupo1,
                    'subgrupo2' : subgrupo2,
                    'subgrupo3' : subgrupo3,
                    'noUsar' : noUsar,
                    'ultimo1': ultimo1,
                    'ultimo2': ultimo2,
                    'ultimo3': ultimo3,
                    'ultimo4': ultimo4,
                    'colorC': colorC,
                    'colorT': colorT,
                    'color1' : color1,
                    'comentario1': comentario1
                    
                })

            
    else:
        
        # return ayudasTto GET----------------------------------------------------------      
        return render(request, 'ayudasTto.html', {'farmacos': farmacos, 'ados':ados })
        # el contexto es necesario para que aparezcan los fármacos en el combobox

    
  

# ------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------
#------------------------------------RENDERIZADO DE PÁGINAS---------------------------------------------
# ------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------

    
def inicioDiabetes(request):    
    return render(request, 'inicioDiabetes.html')

def ado(request):    
    return render(request, 'ado.html')

def ttoAdo(request):    
    return render(request, 'ttoAdo.html')

def ttoDMSAS(request):    
    return render(request, 'ttoDMSAS.html')

def ttoSEMI(request):    
    return render(request, 'ttoSEMI.html')
def insulinizacion(request):    
    return render(request, 'insulinizacion.html')

def insulinas(request):    
    return render(request, 'insulinas.html')

def retinografias(request):    
    return render(request, 'retinografia.html')

def solicitudRetinografias(request):    
    return render(request, 'solicitudRetinografias.html')

def lecturaRetinografias(request):    
    return render(request, 'lecturaRetinografias.html')

def retinopatias(request):    
    return render(request, 'retinopatias.html')

def algoritmoredGDPS(request):    
    return render(request, 'algoritmoredGDPS.html')

def palomares(request):    
    return render(request, 'palomares2021.html')

def informeVisado(request):    
    return render(request, 'informeVisado.html')

def condicionesVisado(request):    
    return render(request, 'condicionesVisado.html')

def insulinizacionSaedyn(request):    
    return render(request, 'insulinizacionSaedyn.html')

def insulinizacionGDPS(request):    
    return render(request, 'insulinizacionRedGDPS2022.html')

def tablaFarmacosFG(request):    
    return render(request, 'tablaFarmacosFG.html')

# ------------------DISPOSITIVOS------------------------------
def solostar(request):    
    return render(request, 'dispositivos/solostar.html')

def novopen(request):    
    return render(request, 'dispositivos/novopen.html')


#-----------------TRATAMIENTO-----------------------------------------
def listadoTtos(request):    
    return render(request, 'ttos/listadoTtos.html')

def tto1(request):    
    return render(request, 'ttos/tto1.html')

def tto2(request):    
    return render(request, 'ttos/tto2.html')




#----------------------------------------------------------
#----------------------------------------------------------




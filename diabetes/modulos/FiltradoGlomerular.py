from ..models import Farmacos

def FG_menor_15():
    # linagliptina = Farmacos.objects.get(farmaco='Linagliptina')
    # glargina = Farmacos.objects.get(farmaco='Insulina glargina')
    # degludec = Farmacos.objects.get(farmaco='Insulina degludec')
    # nuevoFarmaco1 = [linagliptina ]
    # nuevoFarmaco2 = [glargina, degludec ]
    # grupo1 = [nuevoFarmaco1][0][0].grupo
    # grupo2 = [nuevoFarmaco2][0][0].grupo
    # cabecera1= "Elegir entre:"
    # dir1= "#iDPP4"
    # dir2= "#basales"
    # post1= "Se puede usar cualquier iDPP4 excepto saxagliptina. Todos requieren ajuste de dosis excepto linagliptina. Especialmente indicados en paciente frágil."
    # post2 = "(en paciente con glicada lejos del objetivo)"                        
    # pre1 = "Primera opción:"
    # pre2 = "Segunda opción:"
    with open("diabetes/modulos/FG_menor_15.txt","r") as archivo:
        contenido = archivo.read()
        lineas = contenido.split('\n')        
    return(lineas)     
        
    
    
    

def FG_15_30():
    dulaglutida = Farmacos.objects.get(farmaco='Dulaglutida')
    nuevoFarmaco1 = [dulaglutida]
    pre1 = "De elección:"                        
    dir1= "#aGLP1"
    post1 = ". Reduce eventos CV mayores fundamentalmente por la prevención del ictus"
    pioglitazona = Farmacos.objects.get(farmaco='Pioglitazona')
    nuevoFarmaco3 = [pioglitazona]
    pre2 = "Segunda opción:"                        
    dir3= "#pioglitazona"
    post3 = ". Reduce los eventos CV mayores."
    iDPP4 = Farmacos.objects.filter(subgrupo='iDPP4')
    nuevoFarmaco2=[]
    for farmaco in iDPP4:
        nuevoFarmaco2.append(farmaco)
    pre3 = "Tercera opción:"                        
    dir2= "#iDPP4"
    post2 = ". Han demostrado seguridad CV. Linagliptina no requiere ajuste de dosis en IR."
    grupo1 = [nuevoFarmaco1][0][0].grupo
    grupo2 = [nuevoFarmaco2][0][0].grupo
    grupo3 = [nuevoFarmaco3][0][0].grupo
    ultimo1 = nuevoFarmaco1[-1]
    ultimo2 = nuevoFarmaco2[-1]
    ultimo3 = nuevoFarmaco3[-1]
    print("Entre 15 y 30")

def FG_mayor_30():
    print("Mayor de 30")
    
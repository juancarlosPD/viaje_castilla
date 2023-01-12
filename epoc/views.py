from django.shortcuts import render
from django.http import HttpResponse

def inicioEpoc(request):    
    return render(request, 'inicioEpoc.html')

def tratamientoEPOC(request):    
    return render(request, 'EPOCfarmacos.html')

def protocoloEPOC(request):    
    return render(request, 'EPOCprotocolos.html')

def inhaladoresEPOC(request):    
    return render(request, 'EPOCinhaladores.html')

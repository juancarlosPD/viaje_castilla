from django.utils.decorators import method_decorator
from django.http import HttpResponse, JsonResponse
from ast import Try
from urllib import request
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.shortcuts import render, redirect
from datetime import datetime, date
from django.views.generic import View, ListView, TemplateView, UpdateView, CreateView, DeleteView
from crud.forms import PacientesForm, PatologiasForm
from .models import Pacientes, Farmacos, Patologias
from django.urls import reverse_lazy
import csv

# django rest_framework
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, RetrieveUpdateAPIView
from .serializers import PacientesSerializer, Pacientes2Serializer, Pacientes3Serializer

# -----------------API REST FRAMEWORK----------------------------------------

class PacientesListApiView(ListAPIView):

    serializer_class = PacientesSerializer

    def get_queryset(self):
        return Pacientes.objects.all()

class Pacientes3ListApiView(ListAPIView):

    serializer_class = Pacientes3Serializer

    def get_queryset(self):
        return Pacientes.objects.all()
    
class PacientesCreateView(CreateAPIView):

    serializer_class = PacientesSerializer

class PacientesDetailView(RetrieveAPIView):

   serializer_class = PacientesSerializer
   queryset = Pacientes.objects.filter()

class PacientesDeleteView(DestroyAPIView):

    serializer_class = PacientesSerializer
    queryset = Pacientes.objects.all()

# class PacientesUpdateView(UpdateAPIView):  Aquí recupera el paciente en blanco para que actualices todos los datos de nuevo

#     serializer_class = PacientesSerializer
#     queryset = Pacientes.objects.all()

class PacientesUpdateView(RetrieveUpdateAPIView):

    serializer_class = PacientesSerializer
    queryset = Pacientes.objects.all()








# -----------------VISTAS BASADAS EN CLASES----------------------------------------

class Inicio(TemplateView):
    template_name = 'inicio.html'

class InicioCRUD(TemplateView):
    template_name = 'inicioCRUD.html'

class ListarPacientes(ListView):				
    template_name = 'listarPacientes.html'    
    context_object_name = 'pacientes' # Para cambiar objects_list por pacientes   

    def get_queryset(self):
        return Pacientes.objects.all()
    



class ListarDiabeticos(ListView):				
    model = Pacientes
    template_name = 'listarPacientes.html'
    queryset = Pacientes.objects.filter(riesgo_vascular=10)
    context_object_name = 'pacientes' # Para cambiar objects_list por pacientes

class ListarEPOC(ListView):				
    model = Pacientes
    template_name = 'listarPacientes.html'
    queryset = Pacientes.objects.filter(patologia=2)
    context_object_name = 'pacientes' # Para cambiar objects_list por pacientes

class ListarFarmacos(ListView):				
    model = Farmacos
    template_name = 'listarFarmacos.html'
    queryset = Farmacos.objects.all
    context_object_name = 'farmacos' # Para cambiar objects_list por pacientes

    
class ListarPatologias(ListView):				
    model = Patologias
    template_name = 'listarPatologias.html'
    queryset = Patologias.objects.all
    context_object_name = 'patologias' # Para cambiar objects_list por pacientes


class EditarPaciente(UpdateView):
    model = Pacientes
    form_class = PacientesForm
    template_name = 'editarPacientes.html'    
    success_url: reverse_lazy('listarPacientes')  

class CrearPaciente(CreateView):
    model : Pacientes
    form_class = PacientesForm
    template_name = 'editarPacientes.html'    
    success_url: reverse_lazy('listarPacientes')
    

class EliminarPaciente(DeleteView):
    model = Pacientes
    success_url: reverse_lazy('listarPacientes')
    
# -----------------VISTAS BASADAS EN FUNCIONES------------------------------------------------

def inicio(request):
    return render(request, 'inicio.html')

def editarPaciente(request, nuhsa):
    paciente_form = None
    error = None
    try:
        paciente = Pacientes.objects.get(nuhsa=nuhsa)  #Usamos get porque get solo devuelve uno mientras que filter devuelve varios
        nuhsa = paciente.nuhsa
        if request.method =='GET':
            paciente_form = PacientesForm(instance = paciente)
        else:
            paciente_form = PacientesForm(request.POST, instance=paciente)
            if paciente_form.is_valid():
                paciente_form.save()
            return redirect('listarPacientes')
        
    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'crearPaciente.html', {'paciente_form':paciente_form, 'error':error})
    
def eliminarPaciente(request, nuhsa):
    paciente = Pacientes.objects.get(nuhsa=nuhsa)
    nuhsa = paciente.nuhsa
    if request.method == 'POST':        
        paciente.delete()
        return redirect('listarPacientes')
    return render(request, 'eliminarPaciente.html', {'paciente':paciente})


def crearPaciente(request):
    if request.method == 'POST':
        paciente_form = PacientesForm(request.POST)
        if paciente_form.is_valid():
            paciente_form.save()
            print(paciente_form)
            return redirect('listarPacientes')
            
    else:
        paciente_form =PacientesForm()

    
    return render(request, 'crearPaciente.html',{'paciente_form': paciente_form})
    

#  #########################  IMPORT ---  EXPORT  ##################################3
    
def export_csv(request):
    queryset = Farmacos.objects.all()
    options = Farmacos._meta
    fields = [fields.name for fields in options.fields]

    response = HttpResponse(content_type='text/csv')
    response ['Content-Disposition'] = 'atachment; filename="farmacos.csv"'

    writer = csv.writer(response)
    writer.writerow([options.get_field(field).verbose_name for field in fields])

    for obj in queryset:
        writer.writerow([getattr(obj,field) for field in fields])

    return response

def exportP_csv(request):
    queryset = Patologias.objects.all()
    options = Patologias._meta
    fields = [fields.name for fields in options.fields]

    response = HttpResponse(content_type='text/csv')
    response ['Content-Disposition'] = 'atachment; filename="patologias.csv"'

    writer = csv.writer(response)
    writer.writerow([options.get_field(field).verbose_name for field in fields])

    for obj in queryset:
        writer.writerow([getattr(obj,field) for field in fields])

    return response


    






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
from crud.models import Pacientes, Farmacos, Patologias
from django.urls import reverse_lazy

# -----------------VISTAS BASADAS EN CLASES----------------------------------------

class Inicio(TemplateView):
    template_name = 'inicio.html'

class InicioCRUD(TemplateView):
    template_name = 'inicioCRUD.html'

class ListarPacientes(ListView):				
    model = Pacientes
    template_name = 'listarPacientes.html'
    queryset = Pacientes.objects.all
    context_object_name = 'pacientes' # Para cambiar objects_list por pacientes   

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
    

 
    
  

    






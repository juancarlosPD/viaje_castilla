from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
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
from import_export import resources

# django rest_framework
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, RetrieveUpdateAPIView
from .serializers import PacientesSerializer1, PacientesSerializer, Pacientes3Serializer, FarmacoSerializer,  MarcaSerializer, PacientePagination, ContarAnsios

# -----------------API REST FRAMEWORK----------------------------------------

class PacientesListApiView(ListAPIView):

    serializer_class = PacientesSerializer1

    def get_queryset(self):
        return Pacientes.objects.all()
    
class PacientesPaginacionList(ListAPIView):

    serializer_class = PacientesSerializer1
    pagination_class = PacientePagination

    def get_queryset(self):
        return Pacientes.objects.all()
    
class FarmacoDetailView(RetrieveAPIView):

   serializer_class = FarmacoSerializer
   queryset = Pacientes.objects.filter()

class Pacientes3ListApiView(ListAPIView):

    serializer_class = Pacientes3Serializer

    def get_queryset(self):
        return Pacientes.objects.all()
    
class FarmacosListApiView(ListAPIView):

    serializer_class = FarmacoSerializer

    def get_queryset(self):
        return Farmacos.objects.filter(id=38)
    
class FarmacosListApiLink(ListAPIView):

    serializer_class = FarmacoSerializer

    def get_queryset(self):
        return Farmacos.objects.filter(id=38)
    
class NumeroAnsio(ListAPIView):
    serializer_class = ContarAnsios
    def get_queryset(self):
        return Pacientes.objects.cantidad_ansio()
    
class FarmacoDetailView(RetrieveAPIView):

   serializer_class = FarmacoSerializer
   queryset = Pacientes.objects.filter()

    
class PacientesCreateView(CreateAPIView):

    serializer_class = PacientesSerializer1

class PacientesDetailView(RetrieveAPIView):

   serializer_class = PacientesSerializer1
   queryset = Pacientes.objects.filter()

class PacientesDeleteView(DestroyAPIView):

    serializer_class = PacientesSerializer1
    queryset = Pacientes.objects.all()

# class PacientesUpdateView(UpdateAPIView):  Aquí recupera el paciente en blanco para que actualices todos los datos de nuevo

#     serializer_class = PacientesSerializer
#     queryset = Pacientes.objects.all()

class PacientesUpdateView(RetrieveUpdateAPIView):

    serializer_class = PacientesSerializer1
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
    
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data={}

        try:
            #print(request.POST)  # Para ver lo que nos llega desde html (ajax en este caso)
            prueba = request.POST # Para ver lo que nos llega. Es un diccionario
            prueba = request.POST['nuhsa'] # Extraemos el único dato que nos trae el diccionario
            dato = Pacientes.objects.get(nuhsa = prueba) #Traemos un objeto de Pacientes cuyo nuhsa coincida con prueba
            data['nombre'] = dato.nombre

        except Exception as e:
            data['error'] = str(e)
        
        print(dato)
        print(data)
       
        return JsonResponse(data) #Aquí tenemos que pasarle un objeto json, es decir un diccionario. Estos datos los saca en la consola
    
    
class ListarDiabeticos(ListView):
    model = Pacientes
    template_name = 'listarPacientes.html'

    #Las consultas las pasamos en:
    def get_queryset(self):
        return Pacientes.objects.filter(riesgo_vascular=10)
        
    
    #El contexto lo pasamos en:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = 'Listado de diabéticos'
        return context
    
    #Si queremos cambiar el nombre que nos da por defecto para usarlo en el template
    context_object_name = 'pacientes' # Para cambiar objects_list por pacientes	 

    #Método dispatch. Se ejecuta al principio. Redirecciona a POST o GET según la petición
    def dispatch(request, *args, **kwargs):

        return super().dispatch(request, *args, **kwargs)
    
   

class ListarEPOC(ListView):				
    model = Pacientes
    template_name = 'listarPacientes.html'

    #Las consultas las pasamos en:
    @method_decorator(login_required)
    def get_queryset(self):
        return Pacientes.objects.filter(patologia=2)
    
    #El contexto lo pasamos en:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = 'Listado de pacientes con EPOC'
        return context
    
    #Si queremos cambiar el nombre que nos da por defecto para usarlo en el template
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

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     data = {'nombre': 'Juan Carlos'}
    #     return JsonResponse(data)
    

class EliminarPaciente(DeleteView):
    model = Pacientes
    success_url: reverse_lazy('listarPacientes')
    
# -----------------VISTAS BASADAS EN FUNCIONES------------------------------------------------
def eliminarPaciente(request, nuhsa):
    paciente = Pacientes.objects.get(nuhsa=nuhsa)
    nuhsa = paciente.nuhsa
    if request.method == 'POST':        
        paciente.delete()
        return redirect('listarPacientes')
    return render(request, 'eliminarPaciente.html', {'paciente':paciente})


    

#  #########################  IMPORT ---  EXPORT  ##################################3
    
def export_csv(request):

    farmacos_resource = resources.modelresource_factory(model=Farmacos)()
    dataset = farmacos_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response ['Content-Disposition'] = 'atachment; filename="farmacos.csv"'
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


    






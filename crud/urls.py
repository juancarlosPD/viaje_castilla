from django.urls import path, include
from django.contrib.auth.views import LoginView
from crud import views
from crud.views import Inicio, InicioCRUD, ListarPacientes, CrearPaciente, ListarFarmacos, ListarPatologias, ListarDiabeticos, ListarEPOC, export_csv
from crud.models import Pacientes
 

urlpatterns = [
       
    path('crearPaciente/', views.crearPaciente, name='crearPaciente'),
    path('editarPaciente/<str:nuhsa>', views.editarPaciente, name='editarPaciente'),
    path('eliminarPaciente/<str:nuhsa>', views.eliminarPaciente, name='eliminarPaciente'),
   
    path('', Inicio.as_view(), name='inicio'),
    path('InicioCRUD/', InicioCRUD.as_view(), name='inicioCRUD'),
    path('listarPacientes/', ListarPacientes.as_view(), name='listarPacientes'),
    path('diabeticos/', ListarDiabeticos.as_view(), name='diabeticos'),
    path('epoc/', ListarEPOC.as_view(), name='epoc'),
    path('listarPatologias/', ListarPatologias.as_view(), name='listarPatologias'),
    path('listarFarmacos/', ListarFarmacos.as_view(), name='listarFarmacos'),
    path('CrearPaciente/', views.CrearPaciente.as_view(success_url='/listarPacientes/'), name='CrearPaciente'),
    path('EditarPaciente/<str:pk>', views.EditarPaciente.as_view(model=Pacientes, success_url='/listarPacientes/'), name='EditarPaciente'),        
    path('EliminarPaciente/<str:pk>', views.EliminarPaciente.as_view(model=Pacientes, success_url='/listarPacientes/'), name='EliminarPaciente'),
    path('exportar_farmacos', views.export_csv, name='exportar_farmacos'),
    path('exportar_patologias', views.exportP_csv, name='exportar_patologias'),
    ] + [
    
    path('api/paciente3/lista/', views.Pacientes3ListApiView.as_view(), ),
    path('api/paciente/lista/', views.PacientesListApiView.as_view(), name="api/paciente/lista/"),
    path('api/paciente/paginacion/', views.PacientesPaginacionList.as_view(), ),
    path('api/farmaco/detail/<pk>', views.FarmacoDetailView.as_view(), name = 'farmaco_detalle'),
    path('api/farmaco/lista/', views.FarmacosListApiLink.as_view(), name = 'lista_farmacos' ),
    path('api/paciente/create/', views.PacientesCreateView.as_view(), ),
    path('api/paciente/detail/<pk>', views.PacientesDetailView.as_view(), ),    
    path('api/paciente/delete/<pk>', views.PacientesDeleteView.as_view(), ),
    path('api/paciente/update/<pk>', views.PacientesUpdateView.as_view(), ),
    path('numero_ansio/', views.NumeroAnsio.as_view(), ),
    ]


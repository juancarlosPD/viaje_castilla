from django.urls import path, include
from django.contrib.auth.views import LoginView
from crud import views
from crud.views import Inicio, InicioCRUD, ListarPacientes, CrearPaciente, ListarFarmacos, ListarPatologias, ListarDiabeticos, ListarEPOC
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
    
]


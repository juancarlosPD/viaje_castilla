from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crud.urls')),
    path('inicioCRUD', include('crud.urls')),
    path('historia/', include('historia.urls')),
    path('inicioEpoc/', include('epoc.urls')),
    path('inicioDiabetes/', include('diabetes.urls')),
    path('inicioEspecialidades/', include('especialidades.urls')),
    path('inicioCentroSalud/', include('CentroSalud.urls')),
    
]

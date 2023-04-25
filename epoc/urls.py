from django.urls import path
from epoc import views

urlpatterns = [
    path('inicioEpoc/', views.inicioEpoc, name='inicioEpoc'),
    path('tratamientoEPOC/', views.tratamientoEPOC, name='tratamientoEPOC'),
    path('protocoloEPOC/', views.protocoloEPOC, name='protocoloEPOC'),
    path('inhaladoresEPOC/', views.inhaladoresEPOC, name='EPOCinhaladores'),    
]
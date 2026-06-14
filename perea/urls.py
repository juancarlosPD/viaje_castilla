from django.contrib import admin
from django.urls import path, include
from historia.views import inicioHistoria, viaje_castilla

urlpatterns = [
    path('', viaje_castilla, name='inicio'),    
    path('historia/', include('historia.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
    
    




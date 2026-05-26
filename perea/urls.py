from django.contrib import admin
from django.urls import path, include
from historia.views import inicioHistoria

urlpatterns = [
    path('', inicioHistoria, name='inicio'),    
    path('historia/', include('historia.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
    
    




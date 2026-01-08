from django.contrib import admin
from .models import Rey

@admin.register(Rey)
class ReyAdmin(admin.ModelAdmin):
    list_display = ("orden", "nombre", "titulo", "dinastia", "reinado_inicio", "reinado_fin")
    list_filter = ("dinastia", "titulo")
    search_fields = ("nombre", "dinastia", "titulo")
    ordering = ("orden",)
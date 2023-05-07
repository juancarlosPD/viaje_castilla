from django.db import models
from django.db.models import Count

class PacientesAnsio(models.Manager):
    def cantidad_ansio(self):
        resultado = self.values('apellido1').annotate(cantidad=Count('nuhsa'))        
        return resultado

from rest_framework import serializers, pagination
from .models import Pacientes, Patologias, Farmacos, Marca

class PacientesSerializer1(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Pacientes
        fields = (
            'nuhsa',
            'nombre',
            'apellido1',
            'apellido2',            
            'farmaco',
        )
        extra_kwargs = {
            'farmaco' : {'view_name' : 'farmaco_detalle', 'lookup_field' : 'pk'}
        }

class PacientePagination(pagination.PageNumberPagination):
    page_size = 5
    max_page_size = 100

class PacientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pacientes
        fields = ('__all__' )

class FarmacoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Farmacos
        fields = (
            'id',
            'farmaco',
            'grupo',
            'marca',
        )
        
    

class Pacientes2Serializer(serializers.Serializer):
    nuhsa = serializers.CharField(max_length=12)
    nombre = serializers.CharField()
    apellido1 = serializers.CharField()
    apellido2 = serializers.CharField()

class Pacientes3Serializer(serializers.ModelSerializer):
    
    exitus = serializers.BooleanField(default=False)

    class Meta:
        model = Pacientes
        fields = ('__all__' )

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ('__all__' )

class ContarAnsios(serializers.Serializer):
    apellido1 = serializers.CharField()
    cantidad = serializers.IntegerField()



                





from rest_framework import serializers
from .models import Pacientes

class PacientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pacientes
        fields = ('__all__' )

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
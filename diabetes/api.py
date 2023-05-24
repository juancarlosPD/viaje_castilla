
from rest_framework.views import APIView
from rest_framework.response import Response
from crud.models import *

class FarmacosApi(APIView):

    # @transaction.atomic()
    def get(self, request):
        farmacos = Farmacos.objects.all()
        list_farmacos = list()
        for e in farmacos:
            list_farmacos.append({'farmaco':e.farmaco, 'grupo':e.grupo, 'subgrupo':e.subgrupo})

        return Response(list_farmacos)

class SituacionPrincipalApi(APIView):

    # @transaction.atomic()
    def get(self, request):
        situacionprincipal = SituacionClinicaPrincipal.objects.all()
        list_situacionprincipal = list()
        for e in situacionprincipal:
            list_situacionprincipal.append({'situacion':e.situacion, 'id':e.id})

        return Response(list_situacionprincipal)

class SituacionSecundariaApi(APIView):

    # @transaction.atomic()
    def get(self, request):
        situacionprincipal = self.request.GET.get('id')
        situacionsecundaria = SituacionClinicaSecundaria.objects.all()
        if situacionprincipal:
            situacionsecundaria = situacionsecundaria.filter(situacion_principal__id=situacionprincipal)
        list_situacionsecundaria = list()
        for e in situacionsecundaria:
            list_situacionsecundaria.append({'situacion':e.situacion, 'id':e.id})
        return Response(list_situacionsecundaria)

class SituacionTerciariaApi(APIView):

    # @transaction.atomic()
    def get(self, request):
        situacionsecundaria = self.request.GET.get('id')
        situacionterciaria = SituacionClinicaTerciaria.objects.all()
        if situacionsecundaria:
            situacionterciaria = situacionterciaria.filter(situacion_secundaria__id=situacionsecundaria)
        list_situacionterciaria = list()
        for e in situacionterciaria:
            list_situacionterciaria.append({'situacion':e.situacion, 'id':e.id})

        return Response(list_situacionterciaria)
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.core import serializers
from django.http import HttpResponse

from apps.inicio.models import Socio, Capital
from .serializers import CapitalSerializer
import json

def CotizacionWs(request):
    print(request)
    monto = request.GET.get('monto')
    socio = None
    if monto:
        socios = Capital.objects.all().order_by('tasa')
        for obj in socios:
            if float(monto)<=obj.monto_disponible:
                socio = obj
                break
    if socio != None:
        interes = socio.tasa/100
        tasa_efectiva_anual = (((1+interes)**12)-1)*100
        valor_credito = float(monto)*(1+36*interes)
        cuota_mensual = valor_credito/36
        data = {
            'socio' : socio.socio.nombre+' '+socio.socio.apellido, 
            'tasa_efectiva_anual': tasa_efectiva_anual,
            'tasa_efectiva_mensual': socio.tasa,
            'valor_credito': valor_credito,
            'cuota_mensual': cuota_mensual,
            'plazo': '36 Meses'
        }
    else:
        data = {'mensaje': 'No hay socio disponible'}        
    
    dump = json.dumps(data)
    return HttpResponse(dump, content_type='application/json')

class CapitalList(generics.ListCreateAPIView):
    serializer_class = CapitalSerializer
    name = 'capital-list'
    #permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        monto = self.request.GET.get('monto')
        kwargs = {}
        if monto:
            kwargs['monto_disponible__lte'] = monto
        return Capital.objects.filter(**kwargs)        

    def perform_create(self, serializer):
        serializer.save()

class CapitalDetail(generics.RetrieveAPIView):
    queryset = Capital.objects.all()
    serializer_class = CapitalSerializer
    name = 'capital-detail'
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        return Response({
            'socios': reverse(CapitalList.name, request=request),
        })
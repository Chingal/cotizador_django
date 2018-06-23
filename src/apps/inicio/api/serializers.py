from rest_framework import serializers
from django.contrib.auth.models import User
from apps.inicio.models import Socio, Capital

class CapitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capital
        fields = ('url', 'socio', 'monto_disponible', 'tasa', )
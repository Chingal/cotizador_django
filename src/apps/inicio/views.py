from django.shortcuts import render
from .models import Capital

def Home(request):
    monto = request.POST.get('monto')
    socio = 0
    if monto:
        socios = Capital.objects.all().order_by('tasa')
        for obj in socios:
            if float(monto)<=obj.monto_disponible:
                socio = obj
                break
    if socio != 0:
        interes = socio.tasa/100
        tasa_efectiva_anual = (((1+interes)**12)-1)*100
        valor_credito = float(monto)*(1+36*interes)
        cuota_mensual = valor_credito/36
    return render(request, 'inicio/index.html', locals())
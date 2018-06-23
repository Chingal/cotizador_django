from django.urls import path
from .views import ApiRoot, CapitalList, CapitalDetail, CotizacionWs

urlpatterns = [
    path('socios/', CapitalList.as_view(), name=CapitalList.name),
    path('socios/<int:pk>/', CapitalDetail.as_view(), name=CapitalDetail.name),
    path('', ApiRoot.as_view(), name=ApiRoot.name),
    path('ws/cotizacion/', CotizacionWs, name='cotizacion'),
]
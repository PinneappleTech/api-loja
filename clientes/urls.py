from django.urls import path

from .views import ClienteAPIView, EnderecoAPIView

urlpatterns = [
    path('clientes/', ClienteAPIView.as_view(), name='clientes'),
    path('enderecos/', EnderecoAPIView.as_view(), name='enderecos'),
]
from django.urls import path

from . import views

urlpatterns = [
    path('clientes/', views.ClientesGenericView.as_view(), name='clientes'),
    path('clientes/<int:pk>', views.ClienteGenericView.as_view(), name='cliente'),
    path('enderecos/', views.EnderecosGenericView.as_view(), name='enderecos'),
    path('enderecos/<int:pk>', views.EnderecoGenericView.as_view(), name='endereco'),
]
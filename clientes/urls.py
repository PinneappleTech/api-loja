from django.urls import path

from . import views

urlpatterns = [
    path('clientes/', views.ClienteListCreateView.as_view(), name='list_cliente'),
    path('clientes/<int:pk>/', views.ClienteDetailView.as_view(), name='detail_cliente'),
]
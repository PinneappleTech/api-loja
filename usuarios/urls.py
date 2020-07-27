from django.urls import path

from . import views


urlpatterns = [
    path('usuarios/', views.UsuariosGenericView.as_view(), name='usuarios'),
    path('usuarios/<int:pk>/', views.UsuarioGenericView.as_view(), name='usuario'),
]
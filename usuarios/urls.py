from django.urls import path

from . import views

urlpatterns = [
    path('usuarios/', views.UsuariosGenericView.as_view(), name='usuarios'),
]
from django.urls import path

from . import views


urlpatterns = [
    path('', views.UsuariosGenericView.as_view(), name='usuarios'),
    path('<int:pk>/', views.UsuarioGenericView.as_view(), name='usuario'),
]
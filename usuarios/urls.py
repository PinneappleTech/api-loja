from django.urls import path

from . import views


urlpatterns = [
    path('', views.UsuariosGenericView.as_view()),
    path('<int:pk>/', views.UsuarioGenericView.as_view()),
]
from django.urls import path

from . import views


urlpatterns = [
    path('', views.FornecedorListCreateView.as_view()),
    path('<int:pk>/', views.FornecedorDetailView.as_view()),
]
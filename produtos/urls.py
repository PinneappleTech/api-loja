from django.urls import path

from . import views

urlpatterns = [
    path('categorias/', views.CategoriaList.as_view()),
    path('categorias/<int:pk>/', views.CategoriaDetail.as_view()),

    path('marcas/', views.MarcaList.as_view()),
    path('marcas/<int:pk>/', views.MarcaDetail.as_view()),

    path('', views.ProdutoList.as_view()),
    path('<int:pk>/', views.ProdutoDetail.as_view()),
]
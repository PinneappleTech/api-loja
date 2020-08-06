from django.urls import path

from . import views

urlpatterns = [
    path('categorias/', views.CategoriaList.as_view(), name='list_categoria'),
    path('categorias/<int:pk>/', views.CategoriaDetail.as_view(), name='detail_categoria'),

    path('marcas/', views.MarcaList.as_view(), name='list_marca'),
    path('marcas/<int:pk>/', views.MarcaDetail.as_view(), name='detail_marca'),

    path('produtos/', views.ProdutoList.as_view(), name='list_produto'),
    path('produtos/<int:pk>/', views.ProdutoDetail.as_view(), name='detail_produto'),
]
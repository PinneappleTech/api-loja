from django.urls import path

from . import views


urlpatterns = [
    path('', views.ClienteListCreateView.as_view(), name='list_cliente'),
    path('<int:pk>/', views.ClienteDetailView.as_view(), name='detail_cliente'),
]
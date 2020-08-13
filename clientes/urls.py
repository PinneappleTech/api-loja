from django.urls import path

from . import views


urlpatterns = [
    path('', views.ClienteListCreateView.as_view()),
    path('<int:pk>/', views.ClienteDetailView.as_view()),
]
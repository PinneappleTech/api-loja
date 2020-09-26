from django.urls import path

from . import views


urlpatterns = [
    path('', views.VendaList.as_view()),
    path('<int:pk>/', views.VendaDetail.as_view()),
]
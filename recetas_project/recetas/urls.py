"""
URLs de la aplicación recetas
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('recetas/', views.RecetasListView.as_view(), name='recetas_lista'),
    path('receta/<int:pk>/', views.RecetaDetailView.as_view(), name='receta_detalle'),
    path('contacto/', views.contacto, name='contacto'),
    path('confirmacion/', views.confirmacion, name='confirmacion'),
]

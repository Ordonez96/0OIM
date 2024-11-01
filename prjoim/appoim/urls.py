from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('proyecto/<int:proyecto_id>/', views.detalle_proyecto, name='detalle_proyecto'),
]

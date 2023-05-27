
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
	path('crear_conductores/', views.ConductoresCreate.as_view(), name="crear_conductores"),
	path('crear_vehiculos/', views.VehiculosCreate.as_view(), name="crear_vehiculos"),
	path('crear_viajes/', views.ViajesCreate.as_view(), name="crear_viajes"),
	path('nukear_db/', views.nukear_db, name="borrar_data"),
]

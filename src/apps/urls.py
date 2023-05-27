
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
	path('crear_conductores/', views.ConductoresCreate.as_view(), name="crear_conductores"),
]

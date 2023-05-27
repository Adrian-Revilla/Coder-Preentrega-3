from django.shortcuts import render

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView
from . import models

from . import forms, models

def index(request):

	db_data = {
		'Conductores 🧑‍💼': models.Conductor.objects,
		'Viajes 🛣️': models.Viajes.objects,
		'vehiculos 🚗': models.Vehiculo.objects,
	}

	return render(request, 'index.html', context={'data': db_data})



def nukear_db(request):
	models.Vehiculo.objects.all().delete()
	models.Viajes.objects.all().delete()
	models.Conductor.objects.all().delete()
	return redirect("index")

class ConductoresCreate(CreateView):
	model = models.Conductor
	form_class = forms.ConductorForm
	success_url = reverse_lazy("index")
	template_name = "crear_conductores.html"

class VehiculosCreate(CreateView):
	model = models.Vehiculo
	form_class = forms.VehiculoForm
	success_url = reverse_lazy("index")
	template_name = "crear_vehiculos.html"

class ViajesCreate(CreateView):
	model = models.Viajes
	form_class = forms.ViajesForm
	success_url = reverse_lazy("index")
	template_name = "crear_viajes.html"
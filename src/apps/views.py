from django.shortcuts import render

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from . import forms, models

def index(request):
	return render(request, 'index.html')


class ConductoresCreate(CreateView):
	model = models.Conductor
	form_class = forms.ConductorForm
	success_url = reverse_lazy("index")
	template_name = "crear_conductores.html"
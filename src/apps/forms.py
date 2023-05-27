from django import forms

from . import models


class ConductorForm(forms.ModelForm):
	class Meta:
		model = models.Conductor
		fields = "__all__"


class VehiculoForm(forms.ModelForm):
	class Meta:
		model = models.Vehiculo
		fields = "__all__"


class ViajesForm(forms.ModelForm):
	class Meta:
		model = models.Viajes
		fields = "__all__"
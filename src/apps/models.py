from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 


class Vehiculo(models.Model):
	nombre_vehiculo = models.CharField(max_length=100, blank=False, null=False, unique=True)
	fecha_de_fabricacion = models.DateField(blank=False, null=False)
	patente = models.TextField(blank=False, null=False)

	def __str__(self):
		return f"{self.nombre_vehiculo} - {self.fecha_de_fabricacion} - {self.patente} "


class Conductor(models.Model):
	nombre_conductor = models.CharField(max_length=100, null=False, unique=True)
	edad = models.PositiveSmallIntegerField(null=False)


	def __str__(self):
		return f"{self.nombre_conductor} - {self.edad}"


class Viajes(models.Model):
	nombre_del_pasajero = models.CharField(max_length=100, blank=False, null=False, unique=True)
	inicio_viaje = models.DateTimeField(blank=False, null=False)
	fin_viaje = models.DateTimeField(blank=False, null=False)
	medidor_satisfecho = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

	def __str__(self):
		return f"{self.nombre_del_pasajero} - {self.inicio_viaje} - {self.nombre_del_pasajero} - {self.fin_viaje}"
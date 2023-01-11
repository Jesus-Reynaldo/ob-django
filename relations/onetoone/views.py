from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Restaurant

# Create your views here.

def create(request):
  # TODO Crear elementos
  place=Place(name="Lugar 1", address="calle 2005")
  place.save()
  restaurant=Restaurant(place=place,number_of_employees=8)
  restaurant.save()
  
  return HttpResponse(restaurant.place.name)
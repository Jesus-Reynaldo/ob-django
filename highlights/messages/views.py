from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def message(request):
  messages.success(request, 'Hola, soy un mensaje exitoso')
  return render(request, 'messages.html',{})
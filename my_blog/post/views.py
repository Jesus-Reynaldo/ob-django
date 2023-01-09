from django.shortcuts import render
from django.http import HttpResponse
from .models import Author,Entry
# Create your views here.
def queries(request):
  
  #Obtener todo los elementos
  authors = Author.objects.all()
  
  #Obtener datos filtrados por condicion
  filtered=Author.objects.filter(email='virginia75@example.net')
  
  #Obtener un unico objeto(filtrado)
  author=Author.objects.get(id=1)
  
  #Obtener los 10 primeros elementos
  limits = Author.objects.all()[:10]
  
  #Obtener 5 elementos saltando los 5 primeros
  offsets = Author.objects.all()[5:10]
  
  #Obtener todo los elementos
  orders = Author.objects.all().order_by('email')
  
  #Obeter todos los elementos cuyo id sea menor o igual a 15
  filterdLowers=Author.objects.filter(id__lte= 15).order_by('email')
  '''
  __lte : menor o igual (Lower than equals)
  __gte : mayor o igual (Greater than equals)
  __lt  : menor que (Lower than)
  __gt  : mayor que (Greater than)
  __contains : contiene
  __exact : exacto
  '''
  #Obtener todos los autore que contiene la palabra yes
  filteredContains=Author.objects.filter(name__contains= 'some').order_by('email')
  
  
  return render(request, 'post/queries.html',{"authors":authors,"filtered":filtered,"author":author,"limits":limits,"offsets":offsets,"orders":orders,"filteredLowers":filterdLowers,"filteredContains":filteredContains})
  
from django.shortcuts import render
from .models import Product
# Create your views here.
def first(request,letter):
  products = Product.objects.filter(name__istartswith=letter).order_by('name')
  context={
    'products':products,
  }
  return render(request, 'first.html', context)
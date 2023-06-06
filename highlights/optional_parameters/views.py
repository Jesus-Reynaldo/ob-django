from django.shortcuts import render

# Create your views here.
def optional(request,name='Nombre por defecto'):
  context={
    'name':name,
  }
  return render(request,'optional.html',context)
  
from django.http import HttpResponse
from django.shortcuts import render
from .forms import CommentForm, ContactForm

def form(request):
  comment_form = CommentForm({'name': 'Jesus','url': 'http://www.example.com','comment':'Este es un comentario'})
  return render(request, 'form.html',{'comment_form':comment_form})

def goal(request):
  if request.method != 'POST':
    return HttpResponse("Metodo no permitido")
  
  return HttpResponse(request.POST['name'])

def widget(request):
  form = ContactForm()
  return render(request, 'widget.html', {'form': form})
from django.shortcuts import render
from django.http import HttpResponse
from .models import Publication, Article

# Create your views here.
def create(request):
  #en una relacion mucho a muchos primero se debe guardar los dos elementos 
  #que se va a relacionar
  
  art1=Article(headline="Articulo primero")
  art1.save()
  art2=Article(headline="Articulo segundo")
  art2.save()
  art3=Article(headline="Articulo tercero")
  art3.save()
  
  pub1=Publication(title="Publicacion primera")
  pub1.save()
  pub2=Publication(title="Publicacion segunda")
  pub2.save()
  pub3=Publication(title="Publicacion tercera")
  pub3.save()
  pub4=Publication(title="Publicacion cuarta")
  pub4.save()
  pub5=Publication(title="Publicacion quinta")
  pub5.save()
  pub6=Publication(title="Publicacion sexta")
  pub6.save()
  pub7=Publication(title="Publicacion septima")
  pub7.save()
  
  #crear una relacion mucho a muchos
  art1.publications.add(pub1)
  art1.publications.add(pub2)
  art1.publications.add(pub3)
  
  art2.publications.add(pub4)
  art2.publications.add(pub5)
  
  art3.publications.add(pub6)
  art3.publications.add(pub7)
  
  #para eliminar una relacion
  art1.publications.remove(pub2)
  
  result = art1.publications.all()
  
  pub1 = Publication.objects.get(id=1)
  result = pub1.article_set.all()
  
  return HttpResponse(result)
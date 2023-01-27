from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter,Article
from datetime import date
# Create your views here.
def create(request):
  rep=Reporter(
    first_name = "Jesus",
    last_name = "Campos",
    email = "campos@example.com"
  )
  rep.save()
  art1 = Article(headLine="Lorem ipsum dolot",pub_date=date.today(),reporter=rep)
  art1.save()
  art2 = Article(headLine="Lorem set aimet",pub_date=date(2015,6,2),reporter=rep)
  art2.save()
  art3 = Article(headLine="Lorem ipsum set",pub_date=date(2020,4,25),reporter=rep)
  art3.save()
  art4 = Article(headLine="Lorem ipsum",pub_date=date(2000,6,9),reporter=rep)
  art4.save()
  
  #result=art1.reporter.first_name
  result = rep.article_set.all()
  
  
  return HttpResponse(result)

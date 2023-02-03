from django.db import models
from datetime import date
# Create your models here.
class Todo(models.Model):
  title = models.CharField(max_length=100,blank=False,null=False)
  description = models.TextField(blank=True,null=True)
  date = models.DateField(default=date.today)
  estimated_date = models.DateField(blank=True,null=True)
  priority = models.IntegerField(default=3)
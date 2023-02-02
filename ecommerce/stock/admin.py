from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
  #Añadir los atributos de la clase Product
  list_display = ("name","short_description","stock")
  #Añadir una barra de busqueda
  search_fields=("name","short_description",)
  #Añadir un filtro 
  list_filter = ("discount_unit","stock",)
  #Añadir una gerarquia
  date_hierarchy ="discount_unit"

admin.site.register(Product,ProductAdmin)

from django.forms import ModelForm
from .models import Employee


class EmployeeForm(ModelForm):
  class Meta:
    model = Employee
    # fields = ['name', 'last_name', 'email']
    
    #Agregar todo los  campos de un modelo 
    fields ="__all__"
    
    #Agregar una nuevo campo
    #extra_fields =['salary']
    
    #Para excluir un campo
    #exclude = ['email']
  
  
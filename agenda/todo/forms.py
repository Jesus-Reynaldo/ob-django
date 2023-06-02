from django.forms import ModelForm
from .models import Todo
class ContactForm(ModelForm):
  class Meta:
    model = Todo
    fields = '__all__'
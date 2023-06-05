from django.forms import ModelForm
from .models import Contact

class ContactForm(ModelForm):
  class Meta:
    model = Contact
    exclude = ('date',)

  #name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
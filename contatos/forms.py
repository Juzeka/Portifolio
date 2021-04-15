from django import forms
from django.forms import ModelForm
from .models import Contato

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['name','email','motiv','message']
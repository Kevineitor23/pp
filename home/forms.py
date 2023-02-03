from django import forms
from .models import contacto

class MyModelForm(forms.ModelForm):
    class Meta:
        model = contacto
        fields = '__all__'

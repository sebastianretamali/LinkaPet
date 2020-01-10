from django import forms
from .models import Mascota

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota

        fields = ['img','nombre','edad','raza','sexo','tipo', 'estado', 'tamano','personalidad','fundacion','mail_fundacion','descripcion']

class ContactForm(forms.Form):
    from_email = forms.EmailField(max_length=254, required=True, label='Ingrese su email:')
    subject = forms.CharField(max_length=25, label='Ingrese su nombre:', required=True)
    message = forms.CharField(widget=forms.Textarea, max_length=500, label='Ingrese mensaje:', required=True)

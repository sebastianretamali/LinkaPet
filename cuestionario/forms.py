from django import forms
from .models import Cuestionario

#Questionnaire Form
class CuestionarioForm(forms.ModelForm):
    class Meta:
        model = Cuestionario

        fields = ['personalidad', 'cant_ninos', 'edad', 'deportes', 'vivienda']
        labels = {
            'personalidad': ('¿Qué personalidad es la que tienes?'),
            'cant_ninos': ('¿Cuántos niños viven contigo?'),
            'edad': ('¿Qué edad tienes?'),
            'deportes': ('¿Cuántos días a la semana haces deportes?'),
            'vivienda': ('¿En dónde vives?'),

        }
            
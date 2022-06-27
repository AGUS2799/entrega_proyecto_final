from django import forms
from django.forms import ModelForm
from movies.models import Comment

class SeriesForm(forms.Form):
    name = forms.CharField(max_length=40, label='Nombre')
    release_data = forms.DateField(
        label='Fecha de Entrega',
        widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'},)
    )
    director_name = forms.CharField(max_length=40, label='Nombre del director')
    description = forms.CharField(max_length=100, label='Descripción')



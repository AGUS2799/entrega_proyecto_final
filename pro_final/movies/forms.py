from django import forms
from pro_final.widget import DatePickerInput
from django.forms import ModelForm
from movies.models import Comment

class MoviesForm(forms.Form):
    name = forms.CharField(max_length=40, label='Nombre')
    release_data = forms.DateField(widget=DatePickerInput)
    director_name = forms.CharField(max_length=40, label='Nombre del director')
    description = forms.CharField(max_length=100, label='Descripción')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
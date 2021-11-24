from django.forms import ModelForm
from .models import Lead
from django.forms import ModelForm, TextInput, Textarea, NumberInput

class LeadForm(ModelForm):
    class Meta:
       model = Lead
       fields = ['familiyasi', 'ismi', 'yoshi', 'full', 'agent']

       widgets = {
           'familiyasi': TextInput(attrs={
               'class': 'form-control',
               'placeholder': 'Familiyasi'
           }),
           'ismi': TextInput(attrs={
               'class': 'form-control',
               'placeholder': 'Ismi'
           }),
           'yoshi': NumberInput(attrs={
               'class': 'form-control',
               'placeholder': 'Yoshi'
           }),
           'full': Textarea(attrs={
               'class': 'form-control',
               'placeholder': "To'liq ma'lumot"
           }),
       }

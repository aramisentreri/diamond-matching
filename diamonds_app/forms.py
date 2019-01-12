from django import forms
from models import Diamond

class DiamondForm(forms.Form):
    carat = forms.DecimalField(max_digits = 4, decimal_places=2)
    clarity = forms.CharField(max_length = 100)
    color = forms.CharField(max_length = 100)
    cut = forms.CharField(max_length = 100)
    
    

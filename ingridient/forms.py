from django import forms
from .models import IngridientModel


class IngredientForm(forms.ModelForm):
    class Meta:
        model = IngridientModel
        fields = ['name', 'quantity', 'unit', 'recipe']

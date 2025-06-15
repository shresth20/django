from django import forms
from .models import DrinkVariety


class ordersForm(forms.Form):
    orders = forms.ModelChoiceField(
        queryset=DrinkVariety.objects.all(), label="Select Drink Variety")

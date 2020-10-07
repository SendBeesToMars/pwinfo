from django import forms
from django.forms import fields
from .models import Option

class ConfigForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = [
            "capitals",
            "numbers",
            "symbols",
            "min_len",
            "max_len",
            "other_details"            
        ]
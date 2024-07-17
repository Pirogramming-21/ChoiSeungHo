from django import forms
from .models import Develop


class DevelopForm(forms.ModelForm):
    class Meta():
        model = Develop
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

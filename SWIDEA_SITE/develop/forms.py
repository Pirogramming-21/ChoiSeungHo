from django import forms
from .models import Develop


class DevelopForm(forms.ModelForm):
    class Meta():
        model = Develop
        fields = '__all__'

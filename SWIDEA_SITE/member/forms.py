from django import forms
from .models import Member


class MemberForm(forms.ModelForm):
    class Meta():
        model = Member
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
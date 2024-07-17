from django import forms

from develop.models import Develop
from member.models import Member
from .models import Idea


class IdeaForm(forms.ModelForm):
    # member = forms.ModelChoiceField(queryset=Member.objects.all(), label='멤버')  # 없어도 될듯
    # develop = forms.ModelChoiceField(queryset=Develop.objects.all(), label='개발')

    class Meta:
        model = Idea
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

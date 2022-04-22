from django import forms

from .models import User, Equipe, TabelaClassificacao

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class EquipeForm(forms.ModelForm):
    class Meta:
        model = Equipe
        fields = ['nome_time']

class TabelaClassForm(forms.ModelForm):
    class Meta:
        model = TabelaClassificacao
        fields = '__all__'
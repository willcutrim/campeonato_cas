from django import forms

from .models import User, Equipe, Endereco

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nome_completo','numero_telefone','email', 'password', 'equipe']

class EquipeForm(forms.ModelForm):
    class Meta:
        model = Equipe
        fields = ['nome_time']

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = '__all__'
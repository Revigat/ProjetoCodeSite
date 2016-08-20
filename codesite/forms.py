from django import forms
from .models import Pessoa


class PessoaForm(forms.ModelForm):

    class Meta:
        # Qual model vamos usar
        model = Pessoa
        # Nome dos campos do model
        fields = ['nome', 'email', 'mensagem']
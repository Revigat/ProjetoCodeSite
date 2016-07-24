from django import forms 
from .models import Pessoa


class PessoaForm(forms.ModelForm):

	class Meta:
		
		model = Pessoa # qual model vamos usar

		fields = ['nome','email','mensagem'] # nome dos campos do model


# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from codesite.models import Pessoa
from django.core.mail import send_mail
from .forms import PessoaForm


# Create your views here.


@csrf_exempt
def index(request):
	p = Pessoa()

	if request.method == "POST":
		form = PessoaForm(request.POST)
		if form.is_valid():
			vNome = form.cleaned_data['nome'] #é melhor acessar form.cleaned_data. Estes dados não serão somente válidos, mas estarão convertidos em tipos relevantes do Python
			vEmail = form.cleaned_data['email']
			vMensagem = form.cleaned_data['mensagem']
			form.save()
			send_mail('Mensagem de Cliente','Nome: %s \nE-mail: %s \nMensagem: %s '%(vNome,vEmail,vMensagem),'revigatcode@gmail.com',['revigat@gmail.com'])
			send_mail('Code - Inteligência WEB','Agradecemos seu contato e interesse na code, dentro de 24h entraremos em contato.','revigatcode@gmail.com',['%s'%(vEmail)])

			return HttpResponseRedirect('index.html')

	else:

		form = PessoaForm()

	return render_to_response('index.html', {'form' : form })


def apresenta(request):


	usuarios = p.objects.all()

	return render_to_response('apresenta.html',{'usuario': usuarios})

	#return HttpResponse('ok')


def servicos(request):
	return render_to_response('servicos.html')

def cadastro(request):

	p = Pessoa()
	if request.method == "POST":
		nome = request.POST['nome']
		email = request.POST['email']
		p.save()
		return render_to_response('apresenta.html',{'nome': nome , 'email': email})
		

	return render_to_response('cadastro.html')
	



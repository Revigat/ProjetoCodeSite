# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from codesite.models import Pessoa
from django.core.mail import send_mass_mail
from .forms import PessoaForm
# Create your views here.


@csrf_exempt
def index(request):
	p = Pessoa()

	if request.method == "POST":
		form = PessoaForm(request.POST)
		if form.is_valid():
			v_nome = form.cleaned_data['nome'] #é melhor acessar form.cleaned_data. Estes dados não serão somente válidos, mas estarão convertidos em tipos relevantes do Python
			v_email = form.cleaned_data['email']
			v_mensagem = form.cleaned_data['mensagem']
			form.save()
			messages.success(request, 'Profile details updated.')
			msg_adm = ('Mensagem de Cliente','Nome: %s \nE-mail: %s \nMensagem: %s '%(v_nome,v_email,v_mensagem),'revigatcode@gmail.com',['revigat@gmail.com'])
			msg_cliente = ('Code - Inteligência WEB','Agradecemos seu interesse na Code, dentro de 24h entraremos em contato.','revigatcode@gmail.com',['%s'%(v_email)])

			send_mass_mail((msg_adm, msg_cliente), fail_silently=False) #Abre apenas uma conexão com o servidor de email
			return HttpResponseRedirect('index.html')
	else:
		form = PessoaForm()
	return render_to_response('index.html', {'form' : form })


def apresenta(request):
	p = Pessoa()
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

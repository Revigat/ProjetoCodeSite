# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from codesite.models import Pessoa
from django.core.mail import send_mass_mail
from .forms import PessoaForm
# Create your views here.


@csrf_exempt
def index(request):
    if request.method == "POST":
        # Recupera os dados do POST e Cria um objeto de Formulário do tipo PessoaForm
        form = PessoaForm(request.POST)
        # Valida os dados do Formulario
        if form.is_valid():
            '''É melhor acessar form.cleaned_data. Estes dados não serão somente válidos,
                mas estarão convertidos em tipos relevantes do Python'''
            # Recupera cada valor do Dicionario
            vnome = form.cleaned_data['nome']
            vemail = form.cleaned_data['email']
            vmensagem = form.cleaned_data['mensagem']
            # Metodo para salvar no banco de dados
            form.save()
            messages.success(request, 'Profile details updated.')
            # Cria a mensagem para o administrador(CEO)
            msg_adm = ('Mensagem do Cliente', 'Nome: %s \nE-mail: %s \nMensagem: %s ' % (vnome, vemail, vmensagem), 'revigatcode@gmail.com', ['revigat@gmail.com'])
            # Cria a mensagem para o Cliente
            msg_cliente = ('Code - WEB Solutions', 'Agradecemos seu interesse na Code, dentro de 24h entraremos em contato.', 'revigatcode@gmail.com', ['%s' % (vemail)])
            # Abre apenas uma conexão com o servidor de email e evia as duas mensagens
            send_mass_mail((msg_adm, msg_cliente), fail_silently=False)
            # Redireciona para a Index
            return HttpResponseRedirect('index.html')
    else:
        # Se for GET, istancia o Formulário
        form = PessoaForm()
        # Retorna o Formulario renderizado para o Template
        return render_to_response('index.html', {'form': form})


def apresenta(request):
    p = Pessoa()
    usuarios = p.objects.all()
    return render_to_response('apresenta.html', {'usuario': usuarios})


def servicos(request):
    return render_to_response('servicos.html')


def cadastro(request):
    p = Pessoa()
    if request.method == "POST":
        nome = request.POST['nome']
        email = request.POST['email']
        p.save()
        return render_to_response('apresenta.html', {'nome': nome, 'email': email})
    return render_to_response('cadastro.html')

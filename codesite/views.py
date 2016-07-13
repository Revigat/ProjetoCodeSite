from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from codesite.models import Pessoa
#from django.core.mail import send_mail


# Create your views here.


@csrf_exempt
def index(request):
	p = Pessoa()
	if request.method == "POST":
		nome = request.POST['nome']
		email = request.POST['contatoemail']
		mensagem = request.POST['textomsg']
		p.nome = nome
		p.email = email
		p.mensagem = mensagem
		p.save()

		#send_mail('Subject here','Nome: %s \nE-mail: %s \nMensagem: %s '%(p.nome,p.email,p.mensagem),'revigatcode@gmail.com',['revigat@gmail.com,Victor.vh56@gmail.com'])

		return HttpResponseRedirect('index')

		#return render_to_response('index.html')

	return render_to_response('index.html')

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
	



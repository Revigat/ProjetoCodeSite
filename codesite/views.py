from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from codesite.models import Pessoa


# Create your views here.


@csrf_exempt
def index(request):
	p = Pessoa()
	if request.method == "POST":
		nome = request.POST['nome']
		email = request.POST['email']
		p.nome = nome
		p.email = email
		p.save()
		return render_to_response('apresenta.html',{'nome' : nome , 'email' : email})

	return render_to_response('index2.html')

def index2(request):

	return render_to_response('apresenta.html')

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
	



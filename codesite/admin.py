from django.contrib import admin
from codesite.models import *

# Register your models here.

admin.site.register(Pessoa) #Autoriza o django a gerenciar a minha classe
admin.site.register(Cliente)

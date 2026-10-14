from django.contrib import admin
from django.urls import path
from django.shortcuts import render

def cadastro(request):
    return render(request, 'cadastro.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastro/', cadastro, name='cadastro'),
]

# ERRO ENCONTRADO:
# O arquivo cadastro.html não existia no projeto, impedindo o Django de localizar e exibir a página.

# CORREÇÃO:
# Foi criado o arquivo cadastro.html dentro da pasta templates 

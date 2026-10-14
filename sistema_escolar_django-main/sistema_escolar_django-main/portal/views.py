from django.shortcuts import render


def index(request):
  # ERRO ENCONTRADO: O caminho incluía "templates/", o que pode impedir a localização correta do HTML.
    # CORREÇÃO: Removi "templates/" porque o Django procura o arquivo dentro dessa pasta automaticamente.
  return render(request, 'portal/index.html')
from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    #return HttpResponse('Ola Mundo!!')
    return render(request,'index.html')

def articles(request, year):
    return HttpResponse('O ano enviado foi: '+ str(year))

def lerDoBanco(nome):
    lista_nomes = [
        {'nome': 'Ana', 'idade': 30},
        {'nome': 'Pedro', 'idade': 31},
        {'nome': 'Joao', 'idade': 30}
    ]
    for pessoa in lista_nomes:
        if pessoa['nome'] == nome:
            return pessoa
        else:
            return {'nome': 'Nao encontrado', 'idade': 0}
def fname(request, nome):
    result = lerDoBanco(nome)
    if result['idade'] > 0:
        return HttpResponse('A pessoa foi encontrada, ela tem '+ str(result['idade'])+ ' anos')
    else:
        return HttpResponse('Pessoa nao encontrada')

def fname2(request, nome):
    idade = lerDoBanco(nome)['idade']
    return render(request,'pessoa.html',{'v_idade':idade})
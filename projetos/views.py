from xml.sax.handler import property_interning_dict
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Projetos
from django.views import View
import requests

# Create your views here.

def listar_projetos(request):
    projeto = Projetos.objects.all()
    print(projeto)
    return render(request,"projetos/listagem.html",{"projetos":projeto})

# Função para listar projetos em destaque
def listar_projetos_destaque(request):
    projeto = Projetos.Objects.destaque()
    dados = {"projetos": projeto}
    return render(request,"base/base.html",dados)


@login_required(login_url="/accounts/login/")
def projeto(request):
    id_projeto = request.GET.get('id_projeto')
    dados = {}
    if id_projeto:
        dados['projeto'] = Projetos.objects.get(id=id_projeto)
    return render(request,"projetos/cadastro.html",dados)

@login_required(login_url="/accounts/login/")
def Cadastrar_Projeto(request):
    if request.POST:
        nome = request.POST.get("nome")
        tematica = request.POST.get("tematica")
        objetivo = request.POST.get("objetivo")
        justificativa = request.POST.get("justificativa")
        publico_alvo = request.POST.get("publico_alvo")
        id_projeto = request.POST.get("id_projeto")
        if id_projeto:
            Projetos.objects.filter(id=id_projeto).update(nome=nome,
                                                        tematica=tematica,
                                                        objetivo=objetivo,
                                                        justificativa=justificativa,
                                                        publico_alvo=publico_alvo)   
        else:
            Projetos.objects.create(nome=nome,
                                    tematica=tematica,
                                    objetivo=objetivo,
                                    justificativa=justificativa,
                                    publico_alvo=publico_alvo)
    return redirect("/")


def Detalhes_Projeto(request,id=None,*args,**kwargs):
    projeto = get_object_or_404(Projetos,id = id)
    return render(request,"projetos/detalhes.html",{"projeto":projeto})


def baixar_projeto(url, endereco):
    resposta = requests.get(url)
    if resposta.status_code == requests.codes.OK:
        with open(endereco, 'wb') as novo_arquivo:
            novo_arquivo.write(resposta.content)
        print("Donwload finalizado. Salvo em: {}".format(endereco))
    else:
        resposta.raise_for_status()
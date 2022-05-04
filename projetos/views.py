from django.db.models import Q
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Projetos

# Create your views here.

# Função para listar todos projetos
def listar_projetos(request):
    projeto = Projetos.objects.all()
    return render(request,"projetos/listagem.html",{"projetos":projeto})

# Função para listar projetos em destaque
def listar_projetos_destaque(request):
    projeto = Projetos.Objects.destaque()
    return render(request,"base/base.html",{"projetos": projeto})

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

@login_required(login_url="/accounts/login/")
def Detalhes_Projeto(request,id=None,*args,**kwargs):
    projeto = get_object_or_404(Projetos,id = id)
    return render(request,"projetos/detalhes.html",{"projeto":projeto})

def pesquisa(request,*args,**kwargs):
        query = request.GET.get('q',None)
        if query is not None:
            lookups = (Q(nome__icontains = query) | 
                        Q(tematica__icontains = query) | 
                        Q(publico_alvo__icontains = query))
            projeto = Projetos.objects.filter(lookups)
            return render(request,"pesquisa/result_pesquisa.html",{"projetos":projeto, "query":query})
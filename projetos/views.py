from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from .models import Projetos

# Create your views here.

def listar_projetos(request):
    projeto = Projetos.objects.all()
    print(projeto)
    dados = {"projetos": projeto}
    return render(request,"base/home.html",dados)


@login_required(login_url="/accounts/login/")
def projeto(request):
    id_projeto = request.GET.get('id')
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



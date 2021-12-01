from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from .models import Projetos

# Create your views here.

@login_required(login_url="/login/")
def Cadastrar_Projeto(request):
    if request.POST:
        titulo = request.POST.get("titulo")
        descricao = request.POST.get("descricao")
        data_evento = request.POST.get("data_evento")
        local = request.POST.get("local")
        usuario = request.user
        id_evento = request.POST.get("id_evento")
        if id_evento:
            #evento = Evento.objects.get(id=id_evento)
            # if evento.usuario == usuario:
            #     evento.titulo = titulo
            #     evento.descricao = descricao
            #     evento.local = local
            #     evento.data_evento = data_evento
            #     evento.save()
            Projetos.objects.filter(id=id_evento).update(titulo=titulo,
                                                        descricao=descricao,
                                                        data_evento=data_evento,
                                                        local=local)
        else:
            Projetos.objects.create(titulo=titulo,
                                    descricao=descricao,
                                    data_evento=data_evento,
                                    usuario=usuario,
                                    local=local)
    return redirect("projetos/cadastro.html")
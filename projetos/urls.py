from django.urls import path
from .views import Cadastrar_Projeto,projeto,Detalhes_Projeto,listar_projetos,listar_projetos_destaque,pesquisa
app_name = "projetos"

urlpatterns = [
    path("list_projetos/",listar_projetos, name="listar"),
    path("listar/",listar_projetos_destaque, name="destaques"),
    path("listar/<int:id>",Detalhes_Projeto,name="detalhes_projeto"),
    path("projeto/",projeto, name="projeto"),
    path("projeto/submit",Cadastrar_Projeto, name="cadastrar"),
    path("pesquisa/",pesquisa, name="pesquisa"),
]
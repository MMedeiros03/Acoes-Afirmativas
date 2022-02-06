from django.urls import path
from .views import Cadastrar_Projeto,projeto,Detalhes_Projeto,listar_projetos,listar_projetos_destaque,baixar_projeto,pesquisa
app_name = "projetos"

urlpatterns = [
    path("list_projetos/",listar_projetos, name="listar"),
    path("listar/",listar_projetos_destaque, name="destaques"),
    path("listar/<int:id>",Detalhes_Projeto,name="detalhes_projeto"),
    path("projeto/",projeto, name="projeto"),
    path("cadastrar/",Cadastrar_Projeto, name="cadastrar"),
    path("pesquisa/",pesquisa, name="pesquisa"),
    path("baixar_projeto/<url>",baixar_projeto, name="baixar_projeto"),
]
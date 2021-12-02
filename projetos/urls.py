from django.urls import path
from .views import listar_projetos,Cadastrar_Projeto,projeto
app_name = "projetos"

urlpatterns = [
    path("listar/",listar_projetos, name="listar"),
    path("projeto/",projeto, name="projeto"),
    path("projeto/cadastrar/submit",Cadastrar_Projeto, name="cadastrar"),
]
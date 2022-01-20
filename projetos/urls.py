from django.urls import path
from .views import Cadastrar_Projeto,projeto,Detalhes_Projeto,listar_projetos,listar_projetos_destaque
app_name = "projetos"

urlpatterns = [
    path("list_projetos/",listar_projetos, name="listar"),
    path("listar/",listar_projetos_destaque, name="destaques"),
    path("<int:pk>/",Detalhes_Projeto,name="tarefa_detail"),
    path("projeto/",projeto, name="projeto"),
    path("cadastrar/",Cadastrar_Projeto, name="cadastrar"),
]
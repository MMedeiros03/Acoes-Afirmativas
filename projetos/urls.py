from django.urls import path
from .views import listar_projetos,Cadastrar_Projeto,projeto,Detalhes_Projeto
app_name = "projetos"

urlpatterns = [
    path("listar/",listar_projetos, name="listar"),
    path("<int:pk>/",Detalhes_Projeto,name="tarefa_detail"),
    path("projeto/",projeto, name="projeto"),
    path("cadastrar/",Cadastrar_Projeto, name="cadastrar"),
]
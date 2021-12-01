from django.urls import path
from projetos.views import Cadastrar_Projeto
from .views import HomePageView,AcoesAfirmativas

app_name = "pages"

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    #path("projeto/cadastrar/",Cadastrar_Projeto, name="cadastrar"),
    path("acoesafirmativas/",AcoesAfirmativas.as_view(), name="acoes"),
]


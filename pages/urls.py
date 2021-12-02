from django.urls import path
from projetos.views import listar_projetos
from .views import HomePageView,AcoesAfirmativas
from django.views.generic import RedirectView
app_name = "pages"

urlpatterns = [
    path("list/",listar_projetos, name = "list"),
    path('',RedirectView.as_view(url="list/")),
    #path("projeto/cadastrar/",Cadastrar_Projeto, name="cadastrar"),
    path("acoesafirmativas/",AcoesAfirmativas.as_view(), name="acoes"),
]


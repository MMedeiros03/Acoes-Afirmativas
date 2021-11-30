from django.urls import path
from projetos.views import Cadastrar_Projeto
from django.views.generic import RedirectView

app_name = "pages"

urlpatterns = [
    path('',RedirectView.as_view(url="/home/")),
    path("projeto/cadastrar",Cadastrar_Projeto),
]
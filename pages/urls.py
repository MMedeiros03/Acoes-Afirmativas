from django.urls import path
from projetos.views import Cadastrar_Projeto,
from . import views

app_name = "pages"

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("projeto/cadastrar",Cadastrar_Projeto),
]
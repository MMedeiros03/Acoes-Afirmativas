from django.urls import path
from projetos.views import listar_projetos
from .views import AcoesAfirmativas,SobreNos
from django.views.generic import RedirectView
app_name = "pages"

urlpatterns = [
    path("projetos/",listar_projetos, name = "projetos"),
    path('',RedirectView.as_view(url="projetos/")),
    path("acoesafirmativas/",AcoesAfirmativas.as_view(), name="acoes"),
    path("sobrenos/",SobreNos.as_view(),name="sobrenos"),
]


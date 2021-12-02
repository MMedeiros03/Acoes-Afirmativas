from django.urls import path
from .views import listar_projetos

app_name = "projetos"

urlpatterns = [
    path("list/",listar_projetos, name = "list"),
]
from django.views.generic import TemplateView
from projetos.models import Projetos
from django.shortcuts import render
# Create your views here.

class HomePageView(TemplateView):    
    template_name = "base/home.html"

class AcoesAfirmativas(TemplateView):    
    template_name = "acoesafirmativas/teste.html"



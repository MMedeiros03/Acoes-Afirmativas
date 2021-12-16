from django.db.models import query
from django.shortcuts import render
from django.views.generic import ListView
from projetos.models import Projetos
# Create your views here.
class ViewPesquisaProjeto(ListView):
    template_name = "projetos/"
    def get_queryset(self,*args,**kwargs):
        request = self.request
        print("solicitação: ",request)
        resultado = request.GET
        print('resultado: ',resultado)
        query = resultado.get('q',None)
        print("consulta: ",query)
        if query is not None:
            return Projetos.objects.filter(nome__icontains = query)
        return Projetos.objects.none()
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView
from projetos.models import Projetos
# Create your views here.
class ViewPesquisaProjeto(ListView):
    template_name = "pesquisa/result_pesquisa.html"
    def get_context_data(self,*args ,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        query = self.request.GET.get("q")
        context['query'] = query
        return context

    def get_queryset(self,*args,**kwargs):
        request = self.request
        query = request.GET.get('q',None)
        if query is not None:
            projeto = Projetos.Objects.search(query)
            print(projeto)
            return render(request,"pesquisa/result_pesquisa.html",{"projetos":projeto})
        return HttpResponse("deu ruim mane")


        
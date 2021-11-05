from django.shortcuts import render

# Create your views here.

def Pagina_principal(request):    
    return render(request, 'base/base.html')
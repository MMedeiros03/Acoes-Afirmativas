from django.urls import path
from .views import ViewPesquisaProjeto

app_name = "pesquisa"

urlpatterns = [
    path('',ViewPesquisaProjeto.as_view(),name='query')
]
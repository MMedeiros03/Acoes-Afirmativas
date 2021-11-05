from django.urls import path
from .views import Pagina_principal


app_name = "pages"

urlpatterns = [
    path("", Pagina_principal, name="home"),
]
from django.db.models import Q
from django.db import models
from django.urls import reverse
# Create your models here.

class ProjetoQuerySet(models.query.QuerySet):

    def ativo(self): # função para produtos disponiveis
        return self.filter(ativo = True)

    def destaque(self): # função dos produtos em destaque.
        return self.filter(destaque = True, ativo = True)

class ProjetoManager(models.Manager):

    def get_queryset(self):
        return ProjetoQuerySet(self.model, using=self.db)

    def destaque(self):
        return self.get_queryset().destaque()


class Projetos(models.Model):
    nome          = models.CharField(max_length=250,blank=False,null=False)
    tematica      = models.CharField(max_length=250,blank=False,null=False)
    objetivo      = models.CharField(max_length=500,blank=False,null=False)
    justificativa = models.TextField(max_length=2000,blank=False,null=False)
    publico_alvo  = models.CharField(max_length=250,blank=False,null=False)
    data_criacao  = models.DateTimeField(auto_now=True)
    data_atualizacao = models.DateTimeField(auto_now_add=True)
    imagem        = models.ImageField(blank=False,null=False,upload_to='static/imagens/',)
    anexo         = models.FileField(blank=False,null=False,upload_to='static/anexos/')
    ativo         = models.BooleanField(default=False)
    destaque      = models.BooleanField(default=False)
    Objects       = ProjetoManager()
    objects       = ProjetoManager()
    class Meta:
        db_table = "Projeto"
    
    def __str__(self):
        return self.nome
     
    def get_absolute_url(self):
        return reverse("projetos:detalhes_projeto",args=[self.id]) 

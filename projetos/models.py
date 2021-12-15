from django.db import models
from django.db.models.fields.files import ImageField
from django.urls import reverse
# Create your models here.

class Projetos(models.Model):
    nome          = models.CharField(max_length=250,blank=False,null=False)
    tematica      = models.CharField(max_length=250,blank=False,null=False)
    objetivo      = models.CharField(max_length=500,blank=False,null=False)
    justificativa = models.TextField(max_length=2000,blank=False,null=False)
    publico_alvo  = models.CharField(max_length=250,blank=False,null=False)
    data_criacao  = models.DateTimeField(auto_now=True)
    data_atualizacao = models.DateTimeField(auto_now_add=True)
    imagem        = models.ImageField(upload_to='static/imagens/')
    anexo         = models.FileField(upload_to='static/anexos/')

    class Meta:
        db_table = "Projeto"
    
    def __str__(self):
        return self.nome
     
    def get_absolute_url(self):
        return '/projetos/{}/'.format(self.pk)

from django.db import models


class Livro(models.Model):
    categoria = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    foto_capa = models.ImageField(upload_to="fotos/%Y/%m/%d/", null=False)
    autor = models.CharField(max_length=100)
    resumo = models.CharField(max_length=100, null=False, blank=False)

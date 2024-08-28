from django.shortcuts import render
from apps.livros.models import Livro


def index(request):
    livros = Livro.objects.order_by("categoria", "titulo")
    return render(request, "livros/index.html", {"cards": livros})


def buscar(request):
    livros = Livro.objects.order_by("categoria", "titulo")
    return render(request, "livros/index.html", {"cards": livros})

def livro(request, livro_id):
    livros = Livro.objects.order_by("categoria", "titulo")
    return render(request, "livros/index.html", {"cards": livros})

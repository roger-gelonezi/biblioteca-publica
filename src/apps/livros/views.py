from django.shortcuts import render, get_object_or_404
from apps.livros.models import Livro


def index(request):
    livros = Livro.objects.order_by("title")
    return render(request, "livros/index.html", {"cards": livros})


def buscar(request):
    livros = Livro.objects.order_by("title")
    return render(request, "livros/index.html", {"cards": livros})


def livro(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)
    return render(request, "livros/livro.html", {"livro": livro})

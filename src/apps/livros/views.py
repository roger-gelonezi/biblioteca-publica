from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from apps.livros.models import Livro
from apps.livros.forms import ImportarGoogleBooksApiForms
from apps.livros.services.google_books_service import importar_google_books


def index(request):
    livros = Livro.objects.order_by("title")
    return render(request, "livros/index.html", {"cards": livros})


def buscar(request):
    livros = Livro.objects.order_by("title")
    return render(request, "livros/index.html", {"cards": livros})


def livro(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)
    return render(request, "livros/livro.html", {"livro": livro})


def importar_google_books_api(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Você precisa estar logado para utilizar esta ferramenta.")
        return redirect("index")

    form = ImportarGoogleBooksApiForms()
    if request.method == "POST":
        form = ImportarGoogleBooksApiForms(request.POST)
        if form.is_valid():
            isbn_list = form.cleaned_data["isbn_list"].split("\n")
            importar_google_books(isbn_list)
        return redirect("index")
    return render(request, "livros/importar_google_books_api.html", {"form": form})

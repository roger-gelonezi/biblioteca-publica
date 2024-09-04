from django.urls import path
from apps.livros.views import index, buscar, livro, importar_google_books_api

urlpatterns = [
    path("", index, name="index"),
    path("buscar", buscar, name="buscar"),
    path("livro/<int:livro_id>", livro, name="livro"),
    path("importar_google_books_api", importar_google_books_api, name="importar_google_books_api")
]

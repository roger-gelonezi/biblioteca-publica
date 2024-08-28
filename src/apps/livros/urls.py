from django.urls import path
from apps.livros.views import index, buscar, livro

urlpatterns = [
    path("", index, name="index"),
    path("buscar", buscar, name="buscar"),
    path("livro/<int:livro_id>", livro, name="livro"),
]

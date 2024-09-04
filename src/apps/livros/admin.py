from django.contrib import admin
from apps.livros.models import Livro


class ListarLivros(admin.ModelAdmin):
    list_display = ("id", "title", "categories")
    list_per_page = 10


admin.site.register(Livro, ListarLivros)

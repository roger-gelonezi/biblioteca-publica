from django.contrib import admin


from apps.livros.models import Livro

class ListarLivros(admin.ModelAdmin):
    list_display = ("id", "categoria", "titulo")
    list_per_page = 10

admin.site.register(Livro, ListarLivros)

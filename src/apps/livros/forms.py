from django import forms
from apps.livros.models import Livro


class ImportarGoogleBooksApiForms(forms.Form):
    isbn = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), label="ISBN"
    )
    # title = forms.CharField(
    #     widget=forms.TextInput(attrs={"class": "form-control"}), label="Título"
    # )


class LivroForms(forms.ModelForm):
    class Meta:
        model = Livro
        exclude = ["google_books_id"]
        labels = {
            "title": "Título",
            "subtitle": "Subtítulo",
            "authors": "Autores e Tradutores (separados por vírgula)",
            "publisher": "Editora",
            "published_date": "Data de publicação",
            "page_count": "Número de páginas",
            "categories": "Categorias (separadas por vírgula)",
            "language": "Idioma",
            "thumbnail": "Capa do livro",
            "thumbnail_external_url": "URL da capa do livro",
            "isbns": "ISBNs",
            "description": "Descrição",
        }
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "subtitle": forms.TextInput(attrs={"class": "form-control"}),
            "authors": forms.TextInput(attrs={"class": "form-control"}),
            "publisher": forms.TextInput(attrs={"class": "form-control"}),
            "published_date": forms.TextInput(attrs={"class": "form-control"}),
            "page_count": forms.NumberInput(attrs={"class": "form-control"}),
            "categories": forms.TextInput(attrs={"class": "form-control"}),
            "language": forms.TextInput(attrs={"class": "form-control"}),
            "thumbnail": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "thumbnail_external_url": forms.TextInput(attrs={"class": "form-control"}),
            "isbns": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(
                attrs={"class": "form-control", "style": "height: 200px;"}
            ),
        }

    field_order = [
        "title",
        "subtitle",
        "authors",
        "publisher",
        "published_date",
        "page_count",
        "categories",
        "language",
        "thumbnail",
        "thumbnail_external_url",
        "isbns",
        "description",
    ]

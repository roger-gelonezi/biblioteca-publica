import requests
from apps.livros.models import Livro


def __buscar_por_isbn(isbn):
    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
    response = requests.get(url)
    if response.status_code == 200:
        dados_json = response.json()
        totalItens = dados_json.get("totalItems", 0)
        if totalItens == 0:
            return None
        volume = dados_json.get("items", [])[0]

        selfLink = volume.get("selfLink")
        response = requests.get(selfLink)
        dados_json = response.json()

        volumeInfo = dados_json.get("volumeInfo", {})
        volumeInfo["id"] = volume.get("id")
        return volumeInfo


def __salvar_livro(livro):
    livro_model = Livro.objects.get_or_create(google_books_id=livro.get("id"))
    livro_model[0].google_books_id = livro.get("id")
    livro_model[0].title = livro.get("title", "")
    livro_model[0].subtitle = livro.get("subtitle", "")
    livro_model[0].authors = livro.get("authors", [])
    livro_model[0].publisher = livro.get("publisher", "")
    livro_model[0].published_date = livro.get("publishedDate", "")
    livro_model[0].description = livro.get("description", "")
    livro_model[0].page_count = livro.get("pageCount", 0)
    livro_model[0].categories = livro.get("categories", [])
    livro_model[0].language = livro.get("language", "")
    livro_model[0].thumbnail_external_url = livro.get("imageLinks", {}).get("thumbnail")
    livro_model[0].isbns = []
    for isbn in livro.get("industryIdentifiers", []):
        livro_model[0].isbns.append(isbn.get("identifier"))
    livro_model[0].save()


def importar_google_books(isbn):
    livro = __buscar_por_isbn(isbn)
    if livro:
        __salvar_livro(livro)

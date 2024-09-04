from django.db.models import (
    CharField,
    Model,
    IntegerField,
    ImageField,
    DateField,
    TextField,
)
from django_mysql.models import ListTextField


class Livro(Model):
    google_books_id = CharField(max_length=50, unique=True, null=True, blank=True)
    title = CharField(max_length=100)
    subtitle = CharField(max_length=100, null=True, blank=True)
    authors = ListTextField(base_field=CharField(max_length=50), null=True, blank=True)
    publisher = CharField(max_length=50, null=True, blank=True)
    published_date = DateField(null=True, blank=True)
    description = TextField(null=True, blank=True)
    page_count = IntegerField(null=True)
    categories = ListTextField(
        base_field=CharField(max_length=100), null=True, blank=True
    )
    language = CharField(max_length=10, null=True, blank=True)
    thumbnail = ImageField(
        upload_to="fotos/%Y/%m/%d/", null=True, blank=True, max_length=500
    )
    isbn_13 = CharField(max_length=13, null=True, blank=True)
    isbn_10 = CharField(max_length=10, null=True, blank=True)

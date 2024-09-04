from django import forms


class ImportarGoogleBooksApiForms(forms.Form):
    isbn_list = forms.CharField(widget=forms.Textarea())

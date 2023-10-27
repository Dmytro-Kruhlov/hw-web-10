from django import forms

from django.forms import ModelForm, ImageField, FileInput, CharField, TextInput, Textarea

from .models import Author, Quote


class AuthorForm(ModelForm):
    fullname = CharField(max_length=50, widget=TextInput(attrs={"class": "form-control"}))
    born_date = CharField(max_length=50, widget=TextInput(attrs={"class": "form-control"}))
    born_location = CharField(max_length=100, widget=TextInput(attrs={"class": "form-control"}))
    description = TextInput()

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']


class QuoteForm(ModelForm):

    class Meta:
        model = Quote
        fields = ["quote", "tags", "author"]


from django import template
from bson.objectid import ObjectId
from ..utils import get_mongodb
from ..models import Author
register = template.Library()


def get_author(id_):

    author = Author.objects.get(id=id_)
    return author.fullname


register.filter("author", get_author)

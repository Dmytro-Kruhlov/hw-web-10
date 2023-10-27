from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404

from django.core.paginator import Paginator
from .models import Quote, Author, Tag
from .forms import AuthorForm, QuoteForm
from django.contrib.auth.decorators import login_required


def main(request, page=1):
    popular_tags = Tag.objects.annotate(quote_count=Count("quote")).order_by(
        "-quote_count"
    )[:10]
    quotes = Quote.objects.all().order_by("-created_at")
    per_page = 10
    paginator = Paginator(quotes, per_page)
    quotes_on_page = paginator.page(page)
    return render(
        request,
        "quotes/index.html",
        context={"quotes": quotes_on_page, "popular_tags": popular_tags},
    )


@login_required
def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect(to="/")
    else:
        form = AuthorForm()
    return render(request, "quotes/add_author.html", {"form": form})


def author_details(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    return render(request, "quotes/detail.html", {"author": author})


@login_required
def add_quote(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect(to="/")
    else:
        form = QuoteForm()
    return render(request, "quotes/add_quote.html", {"form": form})


def tag(request, tag_name, page=1):
    quotes = Quote.objects.filter(tags__name=tag_name)
    per_page = 10
    paginator = Paginator(quotes, per_page)
    quotes_on_page = paginator.page(page)
    return render(request, "quotes/tag.html", {"quotes": quotes_on_page, "tag_name": tag_name})


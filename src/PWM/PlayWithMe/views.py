from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    # num_books = Book.objects.all().count()
    # num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    # num_instances_available = BookInstance.objects.filter(
        # status__exact="a").count()

    # The 'all()' is implied by default.
    # num_authors = Author.objects.count()

    context = {
        # "num_books": num_books,
        # "num_instances": num_instances,
        # "num_instances_available": num_instances_available,
        # "num_authors": num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, "index.html", context=context)

def search(request):
    """View function for events page of site."""
    # Generate counts of some of the main objects
    # num_books = Book.objects.all().count()
    # num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    # num_instances_available = BookInstance.objects.filter(
    #     status__exact="a").count()

    # The 'all()' is implied by default.
    # num_authors = Author.objects.count()
    #
    # num_events = LibraryEvent.objects.all().count()

    context = {
        # "num_books": num_books,
        # "num_instances": num_instances,
        # "num_instances_available": num_instances_available,
        # "num_authors": num_authors,
        # "num_events": num_events
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, "search.html", context=context)

def results(request):
    """View function for events page of site."""

    context = {
        # "num_books": num_books,
        # "num_instances": num_instances,
        # "num_instances_available": num_instances_available,
        # "num_authors": num_authors,
        # "num_events": num_events
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, "results.html", context=context)

def chat(request):
    """View function for events page of site."""

    context = {
        # "num_books": num_books,
        # "num_instances": num_instances,
        # "num_instances_available": num_instances_available,
        # "num_authors": num_authors,
        # "num_events": num_events
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, "chat.html", context=context)

def post_session(request):
    """View function for events page of site."""

    context = {
        # "num_books": num_books,
        # "num_instances": num_instances,
        # "num_instances_available": num_instances_available,
        # "num_authors": num_authors,
        # "num_events": num_events
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, "post_session_page.html", context=context)

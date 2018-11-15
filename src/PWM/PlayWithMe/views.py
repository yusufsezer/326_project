from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from PlayWithMe.models import Profile, Session, Platform, Game

# Create your views here.
def index(request):
    """View function for home page of site."""
    context = {}

    # Render the HTML template index.html with the data in the context variable
    return render(request, "index.html", context=context)

def search(request):
    """View function for search page of site."""
    platforms = Platform.objects.all()
    games = Game.objects.all()
    locations = set(session.location for session in Session.objects.all())

    context = {
        "platforms": platforms,
        "games": games,
        "locations": locations
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, "search.html", context=context)

def my_groups(request):
    """View function for results page of site."""
    profile_groups = Profile.objects.all()[0].sessions.all()
    def view_group():
        """brings up chat view"""
        chat(request)
    context = {
        "profile_groups": profile_groups,
        "viewgroup": view_group,
    }
    return render(request, "my_groups.html", context=context)

def results(request):
    """View function for results page of site."""
    query_params = request.GET.dict()
    session_list = Session.objects
    to_pop=[]
    for key in query_params:
        if not query_params[key]:
            to_pop.append(key)
    for key in to_pop:
        query_params.pop(key)
    session_list = session_list.filter(**query_params)
    context = {
        "session_list": session_list,
    }
    return render(request, "results.html", context=context)


def post_session(request):
    """View function for events page of site."""
    platforms = Platform.objects.all()
    games = Game.objects.all()
    locations = set(session.location for session in Session.objects.all())
    context = {
        "platforms": platforms,
        "games": games,
        "locations": locations,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, "post_session_page.html", context=context)

# Found this method here:
# https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("index")
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


class SessionDetailView(generic.DetailView):
    model = Session
    template_name = "chat.html"

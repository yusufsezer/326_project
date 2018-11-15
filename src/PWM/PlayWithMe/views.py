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
    profile = Profile.objects.get(user=request.user)
    profile_groups = profile.sessions.all()
    num_groups = len(profile_groups)
    context = {
        "profile_groups": profile_groups,
        "num_groups": num_groups,
    }
    return render(request, "my_groups.html", context=context)

def results(request):
    """View function for results page of site."""
    session_list = Session.objects.all()
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
            new_profile = Profile(user=user)
            new_profile.save()
            return redirect("index")
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

class SessionDetailView(generic.DetailView):
    model = Session
    template_name = "chat.html"

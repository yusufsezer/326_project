from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from PlayWithMe.models import Profile, Session, Platform, Game
import uuid

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
    if "" in locations:
        locations.remove("")

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
    current_profile = Profile.objects.get(user=request.user)
    query_params = request.GET.dict()

    # Delete query parameters that have value None or ""
    to_pop = []
    for key in query_params:
        if not query_params[key]:
            to_pop.append(key)
    for key in to_pop:
        query_params.pop(key)

    # Filter sessions by query parameters and pass the result to the context
    session_list = session_list.filter(**query_params)
    context = {
        "session_list": session_list,
        "current_profile": current_profile,
    }

    # Render the results page
    return render(request, "results.html", context=context)



def post_session(request):
    """View function for post session page of site."""
    platforms = Platform.objects.all()
    games = Game.objects.all()
    locations = set(session.location for session in Session.objects.all())
    if "" in locations:
        locations.remove("")

    context = {
        "platforms": platforms,
        "games": games,
        "locations": locations,
    }

    # Render the post session page
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

def join_session(request, pk):
    print("Joining group...");
    profile = Profile.objects.get(user=request.user)
    session = Session.objects.get(pk=pk)
    profile.sessions.add(session)
    session.profiles.add(profile)
    return session_view(request, pk)

def create_online_session(request):
    """Handler function for the submit button on the post session page's online tab"""
    print("Attempting to create online session...")
    attributes = request.POST.dict()
    attributes["owner"] = Profile.objects.get(user=request.user)
    attributes["online"] = True

    # Attempt to create session; if creation fails, redirect to post session page
    try:
        session = __create_session(attributes)
    except:
        print("Failed to create Session")
        return post_session(request)

    # Redirect the user to the session they just created
    print(f"Created session {session.uuid}")
    return session_view(request, session.pk)

def create_local_session(request):
    """Handler function for the submit button on the post session page's local tab"""
    print("Attempting to create local session...")
    attributes = request.POST.dict()
    attributes["owner"] = Profile.objects.get(user=request.user)
    attributes["online"] = False

    # Attempt to create session; if creation fails, redirect to post session page
    try:
        session=__create_session(attributes)
    except:
        print("Failed to create Session")
        return post_session(request)

    # Redirect the user to the session they just created
    print(f"Created session {session.uuid}")
    return session_view(request, session.pk)

def __create_session(attributes):
    """Utility function for creating Session objects"""
    owner = attributes["owner"]
    session = Session(
        uuid=uuid.uuid4(),
        name=attributes["name"],
        owner=owner,
        online=attributes["online"]
    )
    session.save()

    # Add games if needed
    if attributes["games"]:
        games = Game.objects.get(title=attributes["games"])
        session.games.add(games)

    # Add platforms if needed
    if attributes["platforms"]:
        platforms = Platform.objects.get(name=attributes["platforms"])
        session.platforms.add(platforms)

    # Add location if local session
    if "location" in attributes:
        session.location = attributes["location"]

    # Update the Session and owner's Profile objects as to reflect ownership
    session.profiles.add(owner)
    session.save()
    owner.sessions.add(session)
    owner.sessions_owned.add(session)
    owner.save()

    return session

def session_view(request, pk):
    session = Session.objects.get(pk=pk)

    context = {
        "session": session
    }
    return render(request, "chat.html", context=context)

# class SessionDetailView(generic.DetailView):
#     model = Session
#     template_name = "chat.html"

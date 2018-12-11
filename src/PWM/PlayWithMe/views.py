from django.core.exceptions import ValidationError
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from PlayWithMe.models import Profile, Session, Platform, Game, Message
from django.contrib.auth.models import AnonymousUser
from django import forms
import uuid

def index(request):
    """View function for home page of site."""
    context = {}

    # Render the HTML template index.html with the data in the context variable
    return render(request, "index.html", context=context)

def about_us(request):
    """View function for about page of site."""
    return render(request, "about_us.html")

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
    if not request.user.is_authenticated:
        return signup(request)
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
    }

    # Render the results page
    return render(request, "results.html", context=context)



def post_session(request):
    """View function for post session page of site."""
    if not request.user.is_authenticated:
        return signup(request)
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

# Found this class here:
# https://overiq.com/django-1-10/django-creating-users-using-usercreationform/
class CustomUserCreationForm(forms.Form):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
    email = forms.EmailField(label='Enter email', required=False)
    password1 = forms.CharField(label='Enter password', min_length=6, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', min_length=6, widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user

# Found this method here:
# https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=raw_password, email=email)
            login(request, user)
            new_profile = Profile(user=user)
            new_profile.save()
            return redirect("index")
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def join_session(request, pk):
    print("Joining group...")
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
    profile = Profile.objects.get(user=request.user)
    is_member = True if profile in session.profiles.all() else False
    context = {
        "session": session,
        "profile": profile,
        "is_member": is_member,
    }
    return render(request, "chat.html", context=context)

def send_chat_message(request):
    """Handler for the chat page's send button"""
    print("Attempting to send message...")
    req_body = request.POST.dict()
    session_pk = req_body["session"]
    session = Session.objects.get(pk=session_pk)
    text = req_body["text"][:100]
    sender = Profile.objects.get(user=request.user)
    message = Message(
        text=text,
        sender=sender,
        context=session
    )
    message.save()

    return session_view(request, session_pk)

def delete_message(request):
    print("Attempting to delete message...")
    print(request.POST.dict())
    req_body = request.POST.dict()
    message_pk = req_body["message_pk"]
    session_pk = req_body["session_pk"]
    message = Message.objects.get(pk=message_pk)
    message.delete()
    return session_view(request, session_pk)

# class SessionDetailView(generic.DetailView):
#     model = Session
#     template_name = "chat.html"

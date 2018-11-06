from datetime import timedelta, date
from django.contrib.auth.models import User, Group, Permission
from faker import Faker
from PlayWithMe.models import Platform, Game, Profile, Message, Session
import random
import textwrap
import uuid

fake = Faker()

# Create platforms
platforms = [
    Platform(name="PlayStation 4"),
    Platform(name="XBox One"),
    Platform(name="PC"),
    Platform(name="Nintendo Switch")
]

# Create and save Game objects
games = []
for _ in range(10):
    game_title = fake.text(30)
    game_online = True
    game_description = fake.text(200)
    game_link = fake.text(50)
    game = Game(
        title=game_title,
        online=game_online,
        description=game_description,
        link=game_link,
    )
    game.save()
    games.append(game)

# Create and save Profile objects
profiles = []
for _ in range(15):
    profile_username = fake.user_name() #f"{fake.first_name()}_{fake.last_name()}"
    profile_password = fake.password()
    profile = Profile(
        username=profile_username,
        password=profile_password
    )
    profile.save()
    profiles.append(profile)

# Create and save Session objects
sessions = []
for i in range(10):
    session_id = uuid.uuid4()
    session_location = f"{fake.latitude()}, {fake.longitude()}"
    session_online = True if random.randint(0, 1) == 1 else 0
    session = Session(
        id=session_id,
        location=session_location,
        online=session_online
    )
    session.save()
    sessions.append(session)

# Save Platform objects
for platform in platforms:
    platform.save()

# Randomly associate games with platforms
for platform in platforms:
    num_games = random.randint(1, len(games))
    game_indices = random.sample(range(0, len(games)), num_games)
    for i in game_indices:
        platform.games.add(games[i])
        games[i].platforms.add(platform)
        games[i].save()
    platform.save()

# Randomly associate Games, Platforms, Session with Profiles
for profile in profiles:
    num_platforms = random.randint(1, len(platforms))
    num_games = random.randint(1, len(games))
    num_sessions = random.randint(1, len(sessions))
    platform_indices = random.sample(range(0, len(platforms)), num_platforms)
    game_indices = random.sample(range(0, len(games)), num_games)
    session_indices = random.sample(range(0, len(sessions)), num_sessions)
    for i in platform_indices:
        profile.platforms.add(platforms[i])
    for i in game_indices:
        profile.games.add(games[i])
    for i in session_indices:
        profile.sessions.add(sessions[i])
        sessions[i].profiles.add(profile)
    # for session in sessions:
    #     # print("here: ", type(Profile.session))
    #     owner = Profile.objects.get(sessions=session)
    #     for sess in Profile.sessions:
    #         if sess in owner.sessions:
    #             print('yahooooo!')
    #     owner.sessions_owned.add(session)
    #     session.owner.add(owner)
    profile.save()


# Setup admin user
username = "admin"
password = "admin"
email = "a@a.co"
adminuser = User.objects.create_user(username, email, password)
adminuser.save()
adminuser.is_superuser = True
adminuser.is_staff = True
adminuser.save()

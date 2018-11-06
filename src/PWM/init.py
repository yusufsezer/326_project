from datetime import timedelta, date, datetime
from django.contrib.auth.models import User, Group, Permission
from django.utils import timezone
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

# Save Platform objects
for platform in platforms:
    platform.save()

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
    profile_username = fake.user_name()
    profile_password = fake.password()
    profile = Profile(
        username=profile_username,
        password=profile_password
    )
    profile.save()
    profile_platforms = random.sample(platforms, random.randint(1, len(platforms)))
    for platform in profile_platforms:
        profile.platforms.add(platform)
    profile.save()
    profiles.append(profile)

# Create and save Session objects
sessions = []
for i in range(10):
    session_id = uuid.uuid4()
    session_name = fake.text(50)
    session_location = f"{fake.latitude()}, {fake.longitude()}"
    session_online = True if random.randint(0, 1) == 1 else 0
    session = Session(
        uuid=session_id,
        name=session_name,
        location=session_location,
        online=session_online
    )
    session.save()
    sessions.append(session)

# Randomly associate games, platforms and sessions
for platform in platforms:
    num_games = random.randint(1, len(games))
    game_indices = random.sample(range(0, len(games)), num_games)
    for i in game_indices:
        platform.games.add(games[i])
        games[i].platforms.add(platform)
        games[i].save()
    platform.save()

# Associate sessions with profiles, games and platforms
for session in sessions:
    num_people = random.randint(1, len(profiles))
    people_in_session = random.sample(profiles, num_people)
    session.profiles.set(people_in_session)
    owner = random.sample(people_in_session, 1)[0]
    owner.sessions_owned.add(session)
    session.owner = owner

    for profile in people_in_session:
        profile.sessions.add(session)
        profile.save()
    session.save()

    num_platforms = random.randint(1, len(platforms))
    selected_platforms = random.sample(platforms, num_platforms)
    for platform in selected_platforms:
        session.platforms.add(platform)
    num_games = random.randint(1, len(games) - 1)
    selected_games = random.sample(games, num_games)
    for game in selected_games:
        session.games.add(game)
    session.save()

# Create and save Message objects
messages = []
for i in range(20):
    message_text = fake.text(100)
    message_sender = profiles[random.randint(0, len(profiles) - 1)]
    message_session = message_sender.sessions.all()
    message_session = message_session[random.randint(0, len(message_session)-1)]
    message_time = fake.date_time_this_year(before_now=True, after_now=False, tzinfo=timezone.get_current_timezone())
    message = Message(
        text=message_text,
        sender=message_sender,
        datetime=message_time,
        context=message_session,
    )
    message.save()
    messages.append(message)


# Setup admin user
username = "admin"
password = "admin"
email = "a@a.co"
adminuser = User.objects.create_user(username, email, password)
adminuser.save()
adminuser.is_superuser = True
adminuser.is_staff = True
adminuser.save()

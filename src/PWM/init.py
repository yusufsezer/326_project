from datetime import timedelta, date, datetime
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from faker import Faker
from PlayWithMe.models import Platform, Game, Profile, Message, Session
import random
import textwrap
import uuid
User = get_user_model()

fake = Faker()

# Setup admin user
username = "admin"
password = "admin"
email = "a@a.co"
adminuser = User.objects.create_user(username, email, password)
adminuser.save()
adminuser.is_superuser = True
adminuser.is_staff = True
adminuser.save()
admin_profile = Profile(user=adminuser)
admin_profile.save()

# Setup moderator user
username = "moderator"
password = "moderator"
email = "m@a.co"
moderator_user = User.objects.create_user(username, email, password)
moderator_user.save()
moderator_profile = Profile(user=moderator_user)
moderator_profile.save()

# Create platforms
platforms = [
    Platform(name="PlayStation 4"),
    Platform(name="XBox One"),
    Platform(name="PC"),
    Platform(name="Nintendo Switch")
]

locations = [
    "Center of Campus",
    "Orchard Hill",
    "Central",
    "Northeast",
    "CHC",
    "Southwest",
    "Other",
]

# Save Platform objects
for platform in platforms:
    platform.save()

# Create and save Game objects
game_titles = [
    'FIFA 2018',
    'Fortnite',
    'Minecraft',
    'Rocket League',
    'Call of Duty: Black Ops 4',
    'Forza Horizon 4',
    "Assasin's Creed Odyssey",
    'Far Cry 5',
    'Red Dead Redemption 2',
    'Battlefield 5',
    'Mario Kart 8',
    'Just Dance 2019',
    'Overwatch',
    'Super Smash Bros: Ultimate'
]
games = []
for i in range(len(game_titles)):
    game_title = game_titles[i]
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

moderator_group, created = Group.objects.get_or_create(name='Moderator')
ct = ContentType.objects.get_for_model(Profile)
permission = Permission.objects.create(codename='can_delete_message',
                                       name='Can delete message',
                                       content_type=ct)
moderator_group.permissions.add(permission)
moderator_group.user_set.add(adminuser, moderator_user)  # can take arg for each user

# Create and save Profile objects
profiles = [admin_profile]
for _ in range(15):
    profile_username = fake.user_name()
    profile_user = User(
        username=profile_username,
    )
    profile_user.set_password(fake.password())
    profile_user.save()
    profile = Profile(
        user=profile_user
    )
    profile.save()
    profile_platforms = random.sample(platforms, random.randint(1, len(platforms)))
    for platform in profile_platforms:
        profile.platforms.add(platform)
    profile.save()
    num_games = random.randint(1, len(games))
    selected_games = random.sample(games, num_games)
    for game in selected_games:
        profile.games.add(game)
    profile.save()
    profiles.append(profile)

# Create and save Session objects
sessions = []
session_names = [
    'Elite Game Squad',
    'Northeast Weekly Smash Meetup',
    'Thursday Night Fortnite',
    'Tilted Towers Only',
    'Rocket League tryouts',
    'Southwest Squad',
    'UMass Minecraft server',
    'Saturday FIFA tournaments',
    'Casual just dancing :D',
    'Overwatch 6v6s'
]
for i in range(len(session_names)):
    session_id = uuid.uuid4()
    session_name = session_names[i]
    if session_name is 'Northeast Weekly Smash Meetup':
        session_location="Northeast"
        session_online = False
    else:
        session_location = random.sample(locations, 1)[0]
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
    num_games = random.randint(1, len(games) - 1)
    selected_games = random.sample(games, num_games)
    if session.name is "Northeast Weekly Smash Meetup":
        selected_games = [Game.objects.get(title="Super Smash Bros: Ultimate")]
        selected_platforms = [Platform.objects.get(name="Nintendo Switch")]
    for game in selected_games:
        session.games.add(game)
    for platform in selected_platforms:
        session.platforms.add(platform)
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

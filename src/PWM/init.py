# import textwrap
# import random
# from datetime import timedelta, date

#from django.contrib.auth.models import User, Group, Permission
#from django.contrib.contenttypes.models import ContentType
# from faker import Faker

import textwrap
from datetime import timedelta, date

from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from faker import Faker

from PlayWithMe.models import Profile, Session, Game, Platform, Message



fake = Faker()

# Create platforms
platforms = [
    Platform(name="PlayStation 4"),
    Platform(name="XBox One")
]

# Create games
games = []
for _ in range(10):
    title = fake.text(30)
    platforms = []
    online = True
    description = fake.text(200)
    link = fake.text(50)

# Randomly add games to platforms, and platforms to Games
for platform in platforms:
    k = random.randint(0, len(games) - 1)
    game_indices = random.sample(range(0, len(games) - 1), k)
    platform.games = [games[i] for i in game_indices]

# Save the Platforms
for platform in platforms:
    platform.save()

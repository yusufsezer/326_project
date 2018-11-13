from django.contrib import admin

from PlayWithMe.models import Profile, Session, Game, Platform, Message

class GameInline(admin.TabularInline):
    model = Game

class PlatformInline(admin.TabularInline):
    model = Platform

class MessageInline(admin.TabularInline):
    model = Message

class SessionInline(admin.TabularInline):
    model = Session

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # By setting the list_display variable in an Admin class will have
    # it display only the fields in the model that are specified.
    list_display = ("username",)

    # By setting the fields variable in an Admin class will only
    # display the specified fields in the "detail view" of the
    # model. Fields are displayed vertically by default, but will
    # display horizontally if you further group them in a tuple as we
    # do here for the birth and death dates.
    fields = ["username", "sessions", "sessions_owned", "games", "platforms", "password"]

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "uuid")

    fields = ["name", "owner", "uuid", "profiles", "games", "location", "online", "platforms"]

    inlines = [MessageInline]

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("title",)

    fields = ["title", "online", "description", "platforms", "link"]

    # inlines = [PlatformInline]

@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    list_display = ("name",)

    fields = ["name", "games"]

    # inlines = [GameInline]

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("context", "text", "sender", "datetime")

    fields = ["context", "text", "sender", "datetime"]

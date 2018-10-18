from django.urls import path
from PlayWithMe import views


urlpatterns = [
    path("", views.index, name="index"),
    path("events", views.events, name="events"),
]

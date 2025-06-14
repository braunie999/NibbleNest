from django.apps import AppConfig
from django.contrib import admin


class ReservationsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "reservations"


def ready(self):
    admin.site.site_header = "Restaurant Reservations Admin"
    admin.site.site_title = "Restaurant Reservations Admin Portal"
    admin.site.index_title = (
        "Welcome to the Restaurant Reservations Admin Portal"
    )

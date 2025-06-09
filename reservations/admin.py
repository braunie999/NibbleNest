from django.contrib import admin
from .models import User, RestaurantInfo, Table, Booking, Review


# Register your models here.
admin.site.register(User)
admin.site.register(RestaurantInfo)
admin.site.register(Table)
admin.site.register(Booking)
admin.site.register(Review)
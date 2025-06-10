from django.contrib import admin
from .models import RestaurantInfo, Table, Booking, Review, MenuItem


# Register your models here.
admin.site.register(RestaurantInfo)
admin.site.register(Table)
admin.site.register(Booking)
admin.site.register(Review)
admin.site.register(MenuItem)

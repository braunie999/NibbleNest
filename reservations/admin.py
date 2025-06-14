from django.contrib import admin
from .models import RestaurantInfo, Table, Booking, Review, MenuItem
from django_summernote.admin import SummernoteModelAdmin


class RestaurantInfoAdmin(SummernoteModelAdmin):
    list_display = (
        'name',
        'address',
        'contact_details',
        'opening_hours',
        'description',
        'about_us',
    )


class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'table', 'booking_datetime', 'number_of_guests')
    search_fields = ('user__username', 'table__name')
    list_filter = ('booking_datetime', 'number_of_guests')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'comment', 'timestamp')
    search_fields = ('user__username', 'restaurant__name')
    list_filter = ('rating', 'timestamp')


# Register your models here.
admin.site.register(RestaurantInfo, RestaurantInfoAdmin)
admin.site.register(Table)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(MenuItem)

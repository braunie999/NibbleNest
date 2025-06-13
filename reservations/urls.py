from . import views
from django.urls import path

urlpatterns = [
    path('bookings/', views.booking_list, name='booking_list'),
    path('bookings/create/', views.create_booking, name='create_booking'),
    path(
        'bookings/<int:pk>/update/',
        views.update_booking,
        name='update_booking'
    ),
    path(
        'bookings/<int:pk>/cancel/',
        views.cancel_booking,
        name='cancel_booking'
    ),
]

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    # Inherit default Django auth fields
    pass


class RestaurantInfo(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    contact_details = models.CharField(max_length=200)
    opening_hours = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    about_us = models.TextField(blank=True, null=True)


class Table(models.Model):
    table_number = models.CharField(max_length=50)
    capacity = models.PositiveIntegerField()


class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('rejected', 'Rejected')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    booking_datetime = models.DateTimeField()
    number_of_guests = models.PositiveIntegerField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    special_requests = models.TextField(blank=True, null=True)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
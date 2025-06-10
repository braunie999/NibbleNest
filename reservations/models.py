from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
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

    def __str__(self):
        return f"{self.table_number} ({self.capacity} seats)"


class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('starter', 'Starter'),
        ('salad', 'Salad'),
        ('entree', 'Entrée'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='menu/', blank=True, null=True)
    order = models.PositiveIntegerField(
        default=0,
        help_text="Order in carousel/menu"
    )

    def __str__(self):
        return self.name


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
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-booking_datetime']

    def __str__(self):
        return f"{self.user} | {self.booking_datetime} | {self.table}"


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

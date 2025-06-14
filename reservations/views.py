from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Booking, RestaurantInfo, Review, MenuItem, Table
from .forms import BookingForm, ReviewForm

# Create your views here.


def restaurant_info(request):
    restaurant = get_object_or_404(RestaurantInfo)
    reviews = Review.objects.all().order_by('-timestamp')
    review_form = ReviewForm()
    return render(request, 'reservations/restaurant_info.html', {
        'restaurant': restaurant,
        'reviews': reviews,
        'review_form': review_form,
    })

def home_view(request):
    starters = MenuItem.objects.filter(category='starter')
    salads = MenuItem.objects.filter(category='salad')
    entrees = MenuItem.objects.filter(category='entree')

@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            # Redirect to a booking list or detail view
            return redirect('booking_list')
    else:
        form = BookingForm()

    return render(
        request,
        'reservations/booking_form.html',
        {'form': form}
    )


@login_required
def update_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            # Adjust 'profile' to your actual profile view name if needed
            return redirect('profile')
    else:
        form = BookingForm(instance=booking)
    return render(
        request,
        'reservations/booking_form.html',
        {'form': form}
    )


@login_required
def cancel_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    booking.status = 'cancelled'
    booking.save()
    # Adjust if you want to redirect somewhere else
    return redirect('profile')


@login_required
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(
        request,
        'reservations/booking_list.html',
        {'bookings': bookings}
    )


@login_required
def leave_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
    return redirect('restaurant_info')

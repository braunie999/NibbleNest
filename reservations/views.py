from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Booking
from .forms import BookingForm
# Create your views here.


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

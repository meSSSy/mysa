from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from datetime import datetime
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import Booking
from .forms import BookingForm
from django.views.generic import (
    CreateView,
    ListView,
    DeleteView,
    UpdateView
)


class BookingsPage(LoginRequiredMixin, ListView):
    """
    View booking page
    """
    model = Booking
    template_name = 'booking.html'
    context_object_name = 'bookings'


class CreateBooking(LoginRequiredMixin, CreateView):
    """
    Create a booking for registered users
    """
    model = Booking
    form_class = BookingForm
    template_name = 'booking_create.html'
    success_url = reverse_lazy('booking_page')

    def form_valid(self, form):
        # Set the current user as the booking user
        form.instance.user = self.request.user

        selected_date = form.cleaned_data.get('day')
        selected_time_str = form.cleaned_data.get('time')
        print('selected_time_str', selected_time_str)
        if selected_time_str:
            selected_time = datetime.strptime(selected_time_str, '%I:%M%p').time()
        current_datetime = timezone.now()

        # Check if date is in the past
        if (selected_date < current_datetime.date() or
           (selected_date == current_datetime.date(
                ) and selected_time < current_datetime.time())):
            form.add_error('day', 'Great Scott! Do you have a time machine?')
            return self.form_invalid(form)

        # Check the number of active bookings for the current user
        active_bookings_count = Booking.objects.filter(
            user=self.request.user).count()

        # Limit the maximum number of active bookings to 4
        if active_bookings_count >= 4:
            messages.error(
                self.request,
                "You have reached the maximum number of active bookings."
            )
            return redirect(self.success_url)

        messages.success(self.request, "Your booking has been saved.")
        return super().form_valid(form)


class BookingEdit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Edit an already created booking
    """
    model = Booking
    form_class = BookingForm
    template_name = 'booking_edit.html'
    success_url = reverse_lazy('booking_page')

    def test_func(self):
        booking = self.get_object()
        return self.request.user == booking.user

    def form_valid(self, form):
        form.instance.user = self.request.user
        cleaned_data = form.cleaned_data
        new_date = cleaned_data.get('day')
        new_time = cleaned_data.get('time')

        # Check if the new time and date are available
        if new_date and new_time:
            existing_booking = Booking.objects.filter(
                day=new_date,
                time=new_time).exclude(pk=self.object.pk).first()
            if existing_booking:
                form.add_error('time', 'This time and date is already booked.')
                return self.form_invalid(form)

        messages.success(self.request, "Your booking has been saved.")
        return super().form_valid(form)


class DeleteBooking(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Delete a created Booking
    """
    model = Booking
    template_name = 'booking_confirm_delete.html'
    success_url = reverse_lazy('booking_page')

    def test_func(self):
        booking = self.get_object()
        return self.request.user == booking.user

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Your booking has been deleted.")
        return super().delete(request, *args, **kwargs)


   
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Appointments
from .forms import BookingForm

def booking_page(request):
    return render(request, 'booking.html')

class BookingsPage(LoginRequiredMixin, ListView):
    model = Appointments
    template_name = 'appointment/booking_home_page.html'
    context_object_name = 'appointments'

class CreateBooking(LoginRequiredMixin, CreateView):
    model = Appointments
    form_class = BookingForm
    template_name = 'appointment/booking_create.html'
    success_url = reverse_lazy('booking_page')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        current_datetime = timezone.now()

        if form.instance.day < current_datetime.date() or (
            form.instance.day == current_datetime.date() and
            form.instance.time < current_datetime.time()
        ):
            form.add_error('day', 'Sorry, this is not a valid date and time')
            return self.form_invalid(form)

        active_bookings_count = Appointments.objects.filter(user=self.request.user).count()
        if active_bookings_count >= 2:
            messages.error(self.request, "You have reached the maximum number of active bookings.")
            return redirect(self.success_url)

        messages.success(self.request, "Thank you! Your booking has been saved.")
        return super().form_valid(form)

class BookingEdit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Appointments
    form_class = BookingForm
    template_name = 'appointment/booking_edit.html'
    success_url = reverse_lazy('booking_page')

    def test_func(self):
        booking = self.get_object()
        return self.request.user == booking.user

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        messages.success(self.request, "Thank you! Your booking has been updated.")
        return super().form_valid(form)

class DeleteBooking(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Appointments
    template_name = 'appointment/booking_confirm_delete.html'
    success_url = reverse_lazy('booking_page')

    def test_func(self):
        booking = self.get_object()
        return self.request.user == booking.user

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Your booking has been deleted.")
        return super().delete(request, *args, **kwargs)
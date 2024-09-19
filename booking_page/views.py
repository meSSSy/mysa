from django.shortcuts import render
from django.views.generic import TemplateView

def booking_page(request):
    return render(request, 'booking.html')



from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from datetime import datetime, timedelta
from .models import *
from django.contrib import messages

def booking_page(request):
    return render(request, 'booking.html')
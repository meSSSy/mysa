from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from datetime import datetime, timedelta
from .models import *
from django.contrib import messages

def booking_page(request):
    return render(request, 'booking.html')

def booking(request):
    weekdays = validWeekday(22)
    validateWeekdays = isWeekdayValid(weekdays)

    if request.method == 'POST':
        treatment = request.POST.get('service')
        day = request.POST.get('day')
        if treatment == None:
            messages.success(request, "Please Select A Treatment!")
            return redirect('booking')

        request.session['day'] = day
        request.session['treatment'] = treatment

        return redirect('bookingSubmit')

    return render(request, 'booking.html', {
        'weekdays' :weekdays,
        'validateWeekdays' :validateWeekdays,
    })

def bookingSubmit(request):
    user = request.user
    times = [
        "9 AM", "9:30 AM", "10 AM", "10:30 AM", "11 AM", "11:30", "12 PM", "2 PM", "2:30 PM", "3 PM", "3:30 PM", "4 PM", "4:30 PM", "5 PM"
    ]
    today = datetime.now()
    minDate = today.strftime('%y-%m-%d')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%y-%m-%d')
    maxDate = strdeltatime

    day = request.session.get('day')
    treatment = request.session.get('service')

    hour = checkTime(times, day)
    if request.method == 'POST':
        time = request.POST.get("time")
        date = dayToWeekday(day)

        if treatment != None:
            if day <= maxDate and day >= minDate:
                if date == 'Monday' or date == 'Saturday' or date == 'Wednesday':
                    if Appointment.objects.filter(day=day).count() < 11:
                        if Appointment.objects.filter(day=day, time=time).count() < 1:
                            AppointmentForm = Appointment.objects.get_or_create(
                                user = user,
                                treatment = treatment,
                                day = day,
                                time = time,
                            )
                            messages.success(request, "Appointment Saved!")
                            return redirect('main_page')

                        else:
                            messages.success(request, "The Selected Time Has Already Been Booked!")
                    else:
                        messages.success(request, "Unfortunately This Selected Day Is Full")
                else:
                    messages.success(request, "The Selected Date Is Incorrect")
            else:
                messages.success(request, "The Selected Date Is Not In The Correct Time Period")
        else:
            messages.success(request, "Please Select A Treatment!")

    return render(request, 'profile.html', {
        'times' :hour,
    })
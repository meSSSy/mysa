from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.views import LogoutView

@login_required
def profile_page(request):
    return render(request, 'profile.html')
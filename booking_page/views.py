from django.shortcuts import render
from django.views.generic import TemplateView

from django.shortcuts import render

def index(request):
    return render(request, 'booking.html')

class HomePage(TemplateView):
    """
    Displays home page
    """
    template_name = 'booking.html'

# Create your views here.

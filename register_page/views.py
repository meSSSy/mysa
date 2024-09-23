from django.shortcuts import render
from django.views.generic import TemplateView

def register_page(request):
    return render(request, 'register.html')
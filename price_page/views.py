from django.shortcuts import render
from django.views.generic import TemplateView

def price_page(request):
    return render(request, 'price.html')


from django.shortcuts import render
from django.views.generic import TemplateView


def signin_page(request):
    return render(request, 'login.html')

from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import RegisterForm


def register_page(request):
    return render(request, 'register.html')

def register_page(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/main_page")
    
    else:
        form = RegisterForm()

    return render(response, "register.html", {"form":form})
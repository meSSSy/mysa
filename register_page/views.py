from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm

def register_page(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect("/")
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from signin_page.forms import LoginForm

def signin_page(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/main_page")  # Redirect to main page after successful login
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})
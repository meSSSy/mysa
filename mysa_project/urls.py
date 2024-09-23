"""
URL configuration for mysa_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main_page import views as index_views
from booking_page import views as views
from signin_page import views as views
from price_page import views as views
from register_page import views as views


urlpatterns = [
    path("booking_page/", include("booking_page.urls"), name="booking_page"),
    path("main_page/", include("main_page.urls"), name="main_page"),
    path("signin_page/", include("signin_page.urls"), name="signin_page"),
    path("price_page/", include("price_page.urls"), name="price_page"),
    path("register_page/", include("register_page.urls"), name="register_page"),
    path("admin/", admin.site.urls),
]
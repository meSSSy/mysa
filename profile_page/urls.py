from . import views
from django.contrib.auth.views import LogoutView
from django.urls import path

urlpatterns = [
    path('', views.profile_page, name='profile_page'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
from . import views
from django.urls import path

urlpatterns = [
    path('', views.booking_page, name='booking_page'),
]

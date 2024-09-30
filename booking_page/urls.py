from . import views
from django.urls import path

urlpatterns = [
    path('booking_page/', views.booking_page, name='booking_page'),
]

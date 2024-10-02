from django.urls import path
from . import views

# app_name = 'booking'

urlpatterns = [
    path('', views.BookingsPage.as_view(), name='booking_page'),
    path('create/', views.CreateBooking.as_view(), name='create_booking'),
    path('edit/<int:pk>/', views.BookingEdit.as_view(), name='edit_booking'),
    path('delete/<int:pk>/', views.DeleteBooking.as_view(), name='delete_booking'),
]


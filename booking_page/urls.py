from . import views
from django.urls import path
urlpatterns = [
path('booking_page/', views.index, name='index'),  
    path('', views.HomePage.as_view(), name='booking_page'),  
]
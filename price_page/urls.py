from . import views
from django.urls import path

urlpatterns = [
    path('', views.price_page, name='price_page')
]
from . import views
from django.urls import path

urlpatterns = [
    path('', views.signin_page, name='signin_page')
]
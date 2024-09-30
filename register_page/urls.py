from . import views
from django.urls import path

urlpatterns = [
    path('register_page/', views.register_page, name='register_page')
]
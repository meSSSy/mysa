from . import views
from django.urls import path

urlpatterns = [
    path('', views.register_page, name='register_page')
]
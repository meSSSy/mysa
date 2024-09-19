from . import views
from django.urls import path
urlpatterns = [
path('main_page/', views.index, name='index'),  
    path('', views.HomePage.as_view(), name='main_page'),  
]
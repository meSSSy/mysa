from . import views
from django.urls import path

urlpatterns = [
path('main_page/', index_views.index, name='main'),
    path('booking_page/', views.booking_page, name='booking_page'),
    path('admin/', admin.site.urls),

]
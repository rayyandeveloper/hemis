from django.urls import path

from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('people/<int:pk>/', people_page, name='people'),
    
]
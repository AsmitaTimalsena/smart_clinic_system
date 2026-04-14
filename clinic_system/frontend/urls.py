from django.urls import path

from .views import home,login_page, register, home_page
urlpatterns = [
    path('',home),
    path('login/', login_page),
    path('home/', home_page),
    path('register/', register),

]
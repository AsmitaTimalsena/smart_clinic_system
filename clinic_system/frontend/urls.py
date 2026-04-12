from django.urls import path

from .views import home,login_page
urlpatterns = [
    path('',home),
    path('login/', login_page)
]
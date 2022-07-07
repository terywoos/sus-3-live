from turtle import home
from django.urls import path
from landing import views

urlpatterns = [
    path("",views.landing, name="home")
]
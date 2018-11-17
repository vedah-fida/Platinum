from django.urls import path
from .views import landing
name = "landing"
urlpatterns = [
   path('', landing, name="home-page"),
]
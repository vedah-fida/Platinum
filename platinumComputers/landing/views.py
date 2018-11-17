from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def landing(request):
    msg = "Hello Platinum"
    title = "Platinum Computer Services"
    return render(request, ('landing/landing.html'), {'msg':msg, 'title':title})

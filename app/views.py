from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def jampandu(request):
    return HttpResponse('<h1><marquee>Hi Mama</marquee></h1>')

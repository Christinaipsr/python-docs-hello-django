from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello AZURE Training World CI/CD TESTING !!")

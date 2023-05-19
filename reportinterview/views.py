from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is the report interview View")

# Create your views here.

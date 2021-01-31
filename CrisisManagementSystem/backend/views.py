from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Main Login")

def dashboard(request): 
    return HttpResponse("Dashboard")

def search(request):
    return HttpResponse("Search")

def rank(request):
    return HttpResponse("Ranking Here")
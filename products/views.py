from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return HttpResponse('Hello World')


# To add a new page to the django site
def new(request):
    return HttpResponse('New Products')





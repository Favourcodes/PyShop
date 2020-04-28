from django.http import HttpResponse
from django.shortcuts import render
from. models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


# To add a new page to the django site
def new(request):
    return HttpResponse('New Products')





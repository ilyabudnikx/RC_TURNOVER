from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    prod = Products.objects.all()
    context = {'prod': prod}
    return render(request, 'index.html', context)
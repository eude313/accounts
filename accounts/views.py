from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('home page')

def product(request):
    return HttpResponse('product page')

def customer(request):
    return HttpResponse('customer page')

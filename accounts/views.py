from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('home page')

def product(request):
    return HttpResponse('contact page')

def contact(request):
    return HttpResponse('contact page')

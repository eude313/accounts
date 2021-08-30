from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'account/dashboard.html')

def product(request):
    return HttpResponse('product page')

def customer(request):
    return HttpResponse('customer page')



"""

---accounts --------------
-----templates -----------
-------accounts -----------
----------dashboard.html---
----------product.html------

"""
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'templates/dashboard.html')

def product(request):
    return render(request, 'templates/products.html')

def customer(request):
    return render(request, 'templates/customer.html')



"""

---accounts ---------------
-----templates ------------
-------accounts -----------
----------dashboard.html---
----------product.html-----

"""
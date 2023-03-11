from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def homepage(request):
    return render(request,'home_templates/homepage.html')

def login(request):
    return render(request,'home_templates/login.html')

def sellerlogin(request):
    return render(request,'home_templates/sellerlogin.html')

def customerlogin(request):
    return render(request,'home_templates/customerlogin.html')

def alljewellery(request):
    return render(request,'home_templates/alljewellery.html')

def earrings(request):
    return render(request,'home_templates/earrings.html')

def rings(request):
    return render(request,'home_templates/rings.html')

def necklaces(request):
    return render(request,'home_templates/necklaces.html')

def sample(request):
    return render(request,'home_templates/sample.html')

def master(request):
    return render(request,'home_templates/master.html')

def cus_registration(request):
    return render(request,'home_templates/cus_registration.html')

def sel_registration(request):
    return render(request,'home_templates/sel_registration.html')

# def master(request):
#     return render(request,'home_templates/master.html')



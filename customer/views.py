from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'cus_templates/home.html')

def master(request):
    return render(request,'cus_templates/master.html')

def account(request):
    return render(request,'cus_templates/account.html')

def cart(request):
    return render(request,'cus_templates/cart.html')

def change_pass(request):
    return render(request,'cus_templates/change_pass.html')

def orders(request):
    return render(request,'cus_templates/orders.html')

def sample(request):
    return render(request,'cus_templates/sample.html')

def editprofile(request):
    return render(request,'cus_templates/editprofile.html')

def product_detail(request):
    return render(request,'cus_templates/product_detail.html')

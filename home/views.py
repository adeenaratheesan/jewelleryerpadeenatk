import random
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail
from admins.models import Product
from customer.models import Mycart
from home.models import Customer, Seller
from jewelleryerp import settings


# Create your views here.

# def alljewellery(request):
#     prod_list=Product.objects.all()
#     return render(request,'home_templates/alljewellery.html',{'prod_data':prod_list})
def list_products(request):
    if 'style' in request.GET:
        search_query = request.GET['style']
        print(search_query)
        product_list = Product.objects.filter(style = search_query)

    if 'type' in request.GET:
        
        if 'category' in request.GET:
            product_list = Product.objects.filter(type = request.GET['type'], category = request.GET['category'])
        if 'style' in request.GET:
            product_list = Product.objects.filter(type = request.GET['type'], style = request.GET['style'])
    elif 'category' in request.GET:
        search_query = request.GET['category']
        product_list = Product.objects.filter(category = search_query)

    elif 'items' in request.GET:
        product_list = Product.objects.all()

     
    return render(request,'home_templates/product_list.html',{'data': product_list})
    # return render(request,'home_templates/product_list.html')

def homepage(request):
    return render(request,'home_templates/homepage.html')

def mia(request):
    return render(request,'home_templates/mia.html')

def view_product(request,pid):
    msg=''
    product = Product.objects.get(id=pid)
    if request.method =='POST':
        quantity=request.POST['qty']
        product_exist=Mycart.objects.filter(product=pid,customer=request.session['customer']).exists()
        print(product_exist)
        if not product_exist:
            item = Mycart(customer_id = request.session['customer'],product_id = pid,quantity = quantity)
            item.save()
        else:  
            msg = 'Item already added'
    return render(request,'home_templates/view_product.html',{'product_details':product,'msg':msg})




def customerlogin(request):
    msg=''
    if request.method=="POST":
        c_mail=request.POST['email']
        c_pass=request.POST['password']
        try:
            customer=Customer.objects.get(e_mail=c_mail,password=c_pass)
            request.session['customer']=customer.id
            return redirect('customer:home')
        except:
            msg="Invalid emailid or password!!!!"
    return render(request,'home_templates/customerlogin.html',{'msg':msg})

def master(request,id):
    data=Product.objects.filter().values('category').distinct()
   
    return render(request,'home_templates/master.html',{'prod_data':data})

def view_product(request,pid):

    # to show products
    msg=''
    product = Product.objects.get(id=pid)

    # code to add product in to cart
    # if request.method =='POST':
    #     quantity=request.POST['qty']
    #     product_exist=Mycart.objects.filter(product=pid,customer=request.session['customer']).exists()
    #     print(product_exist)
    #     if not product_exist:
    #         item = Mycart(customer_id = request.session['customer'],product_id = pid,quantity = quantity)
    #         item.save()
    #     else:  
    #         msg = 'Item already added'
            
    # context = {
    #     'product_details':product,
    #     'msg':msg
    # }
    return render (request,'home_templates/view_product.html',{'product_details':product})


    # return render(request,'home_templates/view_product.html')



def cus_registration(request):
    if request.method=='POST':
        cimage=request.FILES['c_img']
        cname=request.POST['c_name']
        cgender=request.POST['c_gender']
        cphone=request.POST['c_phone']
        cemail=request.POST['c_email']
        caddress=request.POST['c_address']
        cpassword=request.POST['c_password']
        new_customer=Customer(
            image=cimage,
            name=cname,
            gender=cgender,
            phone_no=cphone,
            e_mail=cemail,
            address=caddress,
            password=cpassword 
        )
        new_customer.save()
     



    return render(request,'home_templates/cus_registration.html')

def sel_registration(request):
    if request.method=='POST':
        # r_name=request.POST['s_name']
        r_com=request.POST['s_com_name']
        r_address=request.POST['s_address']
        r_mobileno=request.POST['s_mobileno']
        r_email=request.POST['s_email']
        r_logo=request.FILES['s_logo']
        r_bname=request.POST['s_bname']
        r_holder=request.POST['s_holder']
        r_accno=request.POST['s_acnumber']
        r_ifsc=request.POST['s_ifsc']
        r_branch=request.POST['s_branch']
        r_username=random.randint(1111,9999)
        r_password='sel-'+ r_com.lower()+str(r_username)
        message='Hello your username is'+str(r_username)+'add temporary password is'+r_password
        new_seller=Seller(
            company_name=r_com,
            address=r_address,
            mobile=r_mobileno,
            e_mail=r_email,
            company_logo=r_logo,
            bank_name=r_bname,
            acc_name=r_holder,
            accc_no=r_accno,
            ifsc=r_ifsc,
            branch_name=r_branch,
            Username=r_username,
            password=r_password
        )
       
        new_seller.save()
        

    return render(request,'home_templates/sel_registration.html')



# def master(request):
#     return render(request,'home_templates/master.html')


def email_exist(request):
    # email is a variable to store value of emailid given in customer registration
    email=request.POST['email']
# e_mail is the name give for the table in database ,checks this value is equal to the value is input box of email if exits or not this value
# is passed to status and then given to registration page to display
    status=Customer.objects.filter(e_mail=email).exists()
    print(status)
    return JsonResponse({'status':status})
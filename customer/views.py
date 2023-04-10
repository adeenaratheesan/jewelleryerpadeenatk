from tabnanny import check
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from admins.models import Product
from customer.models import Mycart
from django.db.models import F
from home.models import Customer
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request,'cus_templates/home.html')

def logout(request):
    del request.session['cusstomer']
    request.session.flush()
    return redirect('home:homepage')

def master(request):
    return render(request,'cus_templates/master.html')

def account(request):
    account_dt=Customer.objects.get(id=request.session['customer'])
    return render(request,'cus_templates/account.html',{'data':account_dt})
    
def cart(request):
    cartdata=Mycart.objects.filter(customer_id=request.session['customer']).annotate(total=F('product__p_price')*F('quantity'))
    
    grand_total=0
    for i in cartdata:

        grand_total=i.total+grand_total
        request.session['grand']=grand_total
    context={
           'data':cartdata,
            'grandtotal':grand_total
                            }
   
    return render(request,'cus_templates/cart.html',context)

def change_pass(request):
    # updatemsg=''
    # added=''
    # if request.POST:
    #     password=request.POST['old']
    #     newpass=request.POST['newpass']
    #     repass=request.POST['re_pass']
    #     print(password,newpass,repass)
    #     try:
    #         if(newpass==repass):
    #             chek=Customer.objects.get(id=request.session['customer'],password=password)
    #             if check:
    #                 check.password=newpass
    #                 check.save()
    #                 added='password changed'
    #         else:
    #             updatemsg='Old password is not matching'
    #             print('password not matching')
    #     except:
    #         print('passwor error')
    #         updatemsg='password error'

    # ,{'updatemsg': updatemsg,'added':added}
    return render(request,'cus_templates/change_pass.html')


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

     
    return render(request,'cus_templates/product_list.html',{'data':product_list})

# def necklaces(request):
#     product_list=Product.objects.filter(category='Necklace')
#     return render(request,'cus_templates/necklaces.html',{'data':product_list})


def orders(request):
    return render(request,'cus_templates/orders.html')

def cmia(request):
    return render(request,'cus_templates/cmia.html')

# def alljewellery(request):
#     print('*************')
#     prod_list=Product.objects.all()
#     return render(request,'cus_templates/alljewellery.html',{'prod_data':prod_list})

     

def editprofile(request):
    account_dt=Customer.objects.get(id=request.session['customer'])
    if request.POST:
        
        e_name=request.POST['name']
        e_gender=request.POST['c_gender']
        e_phone=request.POST['phone']
        e_email=request.POST['email']
        e_address=request.POST['address']
        updt=Customer.objects.filter(id=request.session['customer']).update(
                                                                          
                                                                           name=e_name,
                                                                           gender=e_gender,
                                                                           phone_no=e_phone,
                                                                           e_mail=e_email,
                                                                           address=e_address)
      
        try:
            e_image=request.FILES['img']
            account_dt.image=e_image
            account_dt.save()
        except:
            e_image=None
        return redirect('customer:editprofile')


    return render(request,'cus_templates/editprofile.html',{'data':account_dt})

# **************************************



def product_detail(request,pid):
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
            
    return render(request,'cus_templates/product_detail.html',{'product_details':product,'msg':msg})

def delete_item(request,pid):
    cart_item=Mycart.objects.get(id=pid)
    cart_item.delete()
    # cartdata=Mycart.objects.filter(id=request.session['customer'])
    # cart_data=Mycart.objects.annotate(total=F('product__p_price')*F('quantity'))
    cartdata=Mycart.objects.filter(customer_id=request.session['customer']).annotate(total=F('product__p_price')*F('quantity'))
    
    grand_total=0
    for i in cartdata:

        grand_total=i.total+grand_total
        request.session['grand']=grand_total
    context={
           'data':cartdata,
            'grandtotal':grand_total
                            }

    return render(request,'cus_templates/cart.html',context)


# def edit_qty(request,pid):
#     cart_item=Mycart.objects.get(id=pid)
#     cart_item.delete()
#     # cartdata=Mycart.objects.filter(id=request.session['customer'])
#     # cart_data=Mycart.objects.annotate(total=F('product__p_price')*F('quantity'))
#     cartdata=Mycart.objects.filter(customer_id=request.session['customer']).annotate(total=F('product__p_price')*F('quantity'))
    
#     grand_total=0
#     for i in cartdata:

#         grand_total=i.total+grand_total
#         request.session['grand']=grand_total
#     context={
#            'data':cartdata,
#             'grandtotal':grand_total
#                             }

#     return render(request,'cus_templates/cart.html',context)
    
#   

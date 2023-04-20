from tabnanny import check
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from admins.models import Product
from customer.models import Mycart, Order, Order_detail
from django.db.models import F
from home.models import Customer
from django.db.models import Q
import razorpay
from jewelleryerp import settings

def delete_item(request,pid):
    print('hhh')
    cart_item=Mycart.objects.get(id=pid)
    print(cart_item.id)
    cart_item.delete()
    return redirect('customer:cart')
# Create your views here.
def home(request):
    return render(request,'cus_templates/home.html')

def logout(request):
    del request.session['customer']
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
    success_msg = ''
    error_msg = ''  
    if request.method == 'POST':
        old_pass = request.POST['old_password']
        new_pass = request.POST['new_password']
        confirm_pass = request.POST['re_password']
        if new_pass == confirm_pass :
            if len(new_pass) >= 8 :
                customer = Customer.objects.get(id = request.session['customer'])
                if customer.password == old_pass :
                    # customer.password = new_pass
                    # customer.save()
                    Customer.objects.filter(id = request.session['customer']).update( password = new_pass )
                    success_msg = 'password changed successfully'
                else:
                    error_msg = 'old password is incorrect'
            else:
                error_msg = 'passwords should be 8 characters'
        else:
            error_msg = 'passwords doesn\'t match'
    return render(request,'cus_templates/change_pass.html',{'success_msg':success_msg,'error_msg':error_msg})


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


def orders(request):
    orders=Order_detail.objects.filter(customer_id=request.session['customer'])
    return render(request,'cus_templates/orders.html',{'orders':orders})


def cmia(request):
    return render(request,'cus_templates/cmia.html')

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

def order_product(request):

    if request.method == "POST":
  
        
        order_amt=request.POST['totalprice']
        order_currency='INR'
       
        notes={'Shipping address':'Bommsnshslli, Bangalore'}
       
        client=razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET))
        payment = client.order.create(
             { "amount": float(order_amt)*100, "currency": "INR", "payment_capture": "1",'notes':notes}
         )
        customer=request.session['customer']
        new_order=Order(
            customer_id=customer,
            amount=request.session['grand'],
            provider_order_id=payment['id'],
            status='pending'

        )
        new_order.save()
        request.session['order_id']=new_order.id
    return JsonResponse(payment)

def updatepayment(request):
    # user_id=request.session['customer']
    # Order.objects.filter(id=request.session['oid'],customer_id=user_id, status='pending').update(status="paid")
    # pid=Order.objects.filter(id=request.session['oid'],customer_id=user_id, status='pending')
    # print('hello')
    # print(pid)
   
    # customer_id=request.session['customer']
    # products=Mycart.objects.filter(customer_id=customer_id) 

    # for pro in products:

    #     print(pro.product)

    #     order=Order_detail(customer_id=customer_id,
    #                 productid_id=pro.product,
    #                 price=pro.product.price,
    #                 quantity=pro.qty,
    #                 status="paid",
    #                 payment_type="Razorpay",
    #                 order_id= pid[0].id,
    #     )
    #     order.save()
    #     products.delete()

    # Order_detail.objects.filter(customer_id=customer_id, status='order_pending',order_id=request.session['oid']).update(status='paid')
   

    # return JsonResponse({'resp':"success"})
    if request.method=='POST':
        # amount=request.POST['grandtotal']
        paymentid=request.POST['pid']
        orderid=request.POST['oid']
        sigid=request.POST['sig']
        orderqty=0
        updateorderDetail=Order.objects.filter(provider_order_id=orderid).update(
            payment_id=paymentid,
            signature_id=sigid,
            status='paid'
        )
        order_id=request.session['order_id']
        cartitem=Mycart.objects.filter(customer=request.session['customer'])
        for singleitem in cartitem:
            new_order_details=Order_detail(
                customer_id=singleitem.customer_id,
                productid_id=singleitem.product_id,
                price=singleitem.product.p_price,
                quantity=singleitem.quantity,
                status='paid',
                payment_type='razorpay',
                order_id=order_id,

                )
            new_order_details.save()
            orderqty=int(singleitem.quantity)
            stockUpdate=Product.objects.get(id=singleitem.product_id)
            stockUpdate.p_stock=stockUpdate.p_stock-orderqty
            stockUpdate.save()
            cartitem.delete()
    return JsonResponse({'halo': 'hii'})

def search(request):
    products = []
    count = 0

    if request.method == 'GET':
        print('in get method')
        searched = request.GET.get('search')
        print(searched)
        if searched:
            products = Product.objects.filter(Q(category__icontains=searched) | Q(p_name__icontains=searched))

            print(products)
            count = products.count()            
    context = {
        'result': products,
        'count':count
    }
    return render(request, 'cus_templates/search.html', context)





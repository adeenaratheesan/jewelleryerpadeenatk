from ssl import ALERT_DESCRIPTION_ACCESS_DENIED
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse

from admins.models import Admins, Category, Product, Style, Type
from home.models import Seller

# Create your views here.
def login(request):
    msg=''
    if request.method=="POST":
        a_username=request.POST['username']
        a_password=request.POST['password']
        try:
            admins=Admins.objects.get(username=a_username,password=a_password)
            request.session['admin']=admins.id
            return redirect('admins:home')
        except:
            msg="Invalid emailid or password!!!!"
    return render(request,'ad_templates/login.html',{'msg':msg})

def logout(request):
    del request.session['admin']
    request.session.flush()
    return redirect('home:homepage')


def home(request):
    account_dt=Seller.objects.get(id=request.session['admin'])
    return render(request,'ad_templates/home.html',{'data':account_dt})

def master(request):
    return render(request,'ad_templates/master.html')

def add_category(request):
    data=Seller.objects.get(id=request.session['admin'])
    if request.method=='POST':
        
        pcategory=request.POST['category']
        pdes=request.POST['description']
        new_category=Category(
            
            Category_name=pcategory,
            description=pdes)
        new_category.save()
    return render(request,'ad_templates/add_category.html',{'categorydt':data})

def add_type(request):
    # sel_data=Seller.objects.get(id=request.session['admin'])
    cate_dt=Category.objects.all()
    if request.method=='POST':
        
        pcategory=request.POST['category']
        ptype=request.POST['type']

        new_type=Type(
            
            category_id=pcategory,
            type=ptype
            )
        new_type.save()
    return render(request,'ad_templates/add_type.html',{'type_dt':cate_dt})

# code for adding type to page add_style
def get_type(request):
    selectedValue=request.POST['selectedValue']
    typ=Type.objects.filter(category_id=selectedValue)
    data=[{'id':typ1.id,'type':typ1.type}for typ1 in typ ]
    # print(selectedValue)
    
    return JsonResponse({'data':data})
def add_style(request):
    cate_dt=Category.objects.all()

    if request.method=='POST':
        
        pcategory=request.POST['category']
        ptype=request.POST['type']
        pstyle=request.POST['style']

        new_style=Style(
            
            category_id=pcategory,
            type_id=ptype,
            style=pstyle
            )
        new_style.save()
    return render(request,'ad_templates/add_style.html',{'styledata':cate_dt})
# upto here

def sample(request):
    return render(request,'ad_templates/sample.html')

def get_addproduct(request):
    
    selectedValue2=request.POST['selectedValue2']
    product=Style.objects.filter(type_id=selectedValue2)
    datas=[{'id':prd.id,'type':prd.type}for prd in product ]
    # print(selectedValue)
    
    return JsonResponse({'datas':datas})
def add_products(request):
    data=Category.objects.all()
    data2=Type.objects.all()
   
    if request.method=='POST':
        
        pcategory=request.POST['category']
        ptype=request.POST['type']
        pstyle=request.POST['style']
        pname=request.POST['s_pname']
        pnum=request.POST['s_pid']
        pdescription=request.POST['s_pdesc']
        pstock=request.POST['s_pstock'] 
        pprice=request.POST['s_pprice']
        pimg=request.FILES['s_pimg']
        new_product=Product(
            
            category=pcategory ,
            type=ptype,
            style=pstyle,
            p_name= pname,
            p_number=pnum,
            description=pdescription,
            p_stock= pstock,
            p_price=pprice,
            p_image= pimg
        )
       
        new_product.save()
    return render(request,'ad_templates/add_products.html',{'addcategory':data,'addtype':data2})

def order_his(request):
    return render(request,'ad_templates/order_his.html')

def change_pass(request):
    
    return render(request,'ad_templates/change_pass.html')

def product_catelogue(request):
    product_dt=Product.objects.all
    return render(request,'ad_templates/product_catelogue.html',{'data':product_dt})

#  product_details=Product.objects.filter(seller_id=request.session['seller'])
#     return render(request,'sel_templates/product_catelogue.html',{'data':product_details})

def recent_orders(request):
    return render(request,'ad_templates/recent_orders.html')

def update_stock(request,pid):
    msg=''
    updstk=''
    product = Product.objects.get(id=pid)
    
    if request.POST:
        p_stk=request.POST['cstock']
        updstk = Product.objects.filter(id=pid).update(p_stock=p_stk)
        return redirect('admins:product_catelogue')    
    return render(request,'ad_templates/update_stock.html',{'stk':updstk,'data':product})

def edit_profile(request):
    account_dt=Seller.objects.get(id=request.session['admin'])
    if request.POST:
        e_c_name=request.POST['company_name']
        e_address=request.POST['address']
        e_phone=request.POST['phone']
        e_email=request.POST['e_mail']
        e_bname=request.POST['bank_name']
        e_hname=request.POST['acc_name']
        e_acno=request.POST['accc_no']
        e_ifsc=request.POST['ifsc']
        e_branch=request.POST['branch_name']
        updt=Seller.objects.filter(id=request.session['admin']).update(
                                                                        
                                                                        company_name=e_c_name,
                                                                        address=e_address,
                                                                        mobile=e_phone,
                                                                        e_mail=e_email,
                                                                        bank_name=e_bname,
                                                                        acc_name=e_hname,
                                                                        accc_no=e_acno,
                                                                        ifsc=e_ifsc,
                                                                        branch_name=e_branch

                                                                       
                                                                           )
        try:
            e_image=request.FILES['company_logo']
            account_dt.company_logo=e_image
            account_dt.save()
        except:
            e_image=None
        return redirect('admins:edit_profile')
        # msg="Updated successfully"
    
    return render(request,'ad_templates/edit_profile.html',{'data':account_dt})

   
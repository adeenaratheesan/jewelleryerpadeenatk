from django.urls import path
from .import views
app_name='home'

urlpatterns=[
    path('homepage/',views.homepage,name='homepage'),
    path('customerlogin/',views.customerlogin,name='customerlogin'),
    # path('view_product/',views.view_product,name='view_product'),
    path('master/',views.master,name='master'),
    path('cus_registration/',views.cus_registration,name='cus_registration'),
    path('sel_registration/',views.sel_registration,name='sel_registration'),
    path('mia/',views.mia,name='mia'),
    path('email_exist/',views.email_exist,name='email_exist'),
    path('view_product/<int:pid>',views.view_product,name='view_product'),
    path('product/list',views.list_products,name='list_products'),
    # path('gold/',views.gold,name='gold'),
    # path('diamond/',views.diamond,name='diamond'),
    # path('hoops_huggies/',views.hoops_huggies,name='hoops_huggies'),
    # path('jhumkas/',views.jhumkas,name='jhumkas'),
    # path('stud/',views.stud,name='stud'),
    # path('mangalsutra/',views.mangalsutra,name='mangalsutra'),
    # path('traditional/',views.traditional,name='traditional'),
    # path('bib/',views.bib,name='bib'),
    # path('alljewellery/',views.alljewellery,name='alljewellery'),
    # path('earrings/',views.earrings,name='earrings'),
    # path('rings/',views.rings,name='rings'),
    # path('necklaces/',views.necklaces,name='necklaces'),
                  
                  
]
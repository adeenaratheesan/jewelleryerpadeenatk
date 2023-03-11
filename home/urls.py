from django.urls import path
from .import views
app_name='home'

urlpatterns=[
    path('homepage/',views.homepage,name='homepage'),
    path('login/',views.login,name='login'),
    path('sellerlogin/',views.sellerlogin,name='sellerlogin'),
    path('customerlogin/',views.customerlogin,name='customerlogin'),
    path('alljewellery/',views.alljewellery,name='alljewellery'),
    path('earrings/',views.earrings,name='earrings'),
    path('rings/',views.rings,name='rings'),
    path('necklaces/',views.necklaces,name='necklaces'),
    path('sample/',views.sample,name='sample'),
    path('master/',views.master,name='master'),
    path('cus_registration/',views.cus_registration,name='cus_registration'),
    path('sel_registration/',views.sel_registration,name='sel_registration'),
    # path('master/',views.master,name='master'),
                  
]
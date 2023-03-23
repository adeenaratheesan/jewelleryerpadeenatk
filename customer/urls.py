from django.urls import path
from .import views
app_name='customer'

urlpatterns=[
   path('home/',views.home,name='home'),
   path('master/',views.master,name='master'),
   path('account/',views.account,name='account'),
   path('cart/',views.cart,name='cart'),
   path('change_pass/',views.change_pass,name='change_pass'),
   path('orders/',views.orders,name='orders'),
   path('sample/',views.sample,name='sample'),
   path('editprofile/',views.editprofile,name='editprofile'),
   path('product_detail/',views.product_detail,name='product_detail'),


]
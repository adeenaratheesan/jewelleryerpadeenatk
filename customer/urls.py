from django.urls import path
from .import views
app_name='customer'

urlpatterns=[
   path('home/',views.home,name='home'),
   path('master/',views.master,name='master'),
   path('account/',views.account,name='account'),
   path('cart/',views.cart,name='cart'),
   path('logout/',views.logout,name='logout'),
   path('change_pass/',views.change_pass,name='change_pass'),
   path('orders/',views.orders,name='orders'),
   path('product/list',views.list_products,name='list_products'),
   path('editprofile/',views.editprofile,name='editprofile'),
   path('product_detail/<int:pid>',views.product_detail,name='product_detail'),
   path('delete_item/<int:pid>',views.delete_item,name='delete_item'),
   path('cmia/',views.cmia,name='cmia'),
  


]
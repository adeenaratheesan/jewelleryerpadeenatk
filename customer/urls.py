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

   path('order_product/',views.order_product,name='order_product'),
   path('updatepayment/',views.updatepayment,name='updatepayment'),



   path('search/',views.search,name='search'),
   # path('change_qty',views.change_qty,name="change_qty"),

   # path('orderpayment/',views.orderpayment,name='orderpayment'),
   # path('update_payment/',views.update_payment,name='update_payment'),
   # path('pay/',views.pay,name='pay'),
   # path('update/',views.update,name='update'),

   


]
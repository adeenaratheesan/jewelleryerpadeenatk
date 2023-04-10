from django.urls import path
from .import views
app_name='admins'


urlpatterns=[
   path('login/',views.login,name='login'),
   path('home/',views.home,name='home'),
   path('master/',views.master,name='master'),
   path('add_products/',views.add_products,name='add_products'),
   path('order_his/',views.order_his,name='order_his'),
   path('change_pass/',views.change_pass,name='change_pass'),
   path('product_catelogue/',views.product_catelogue,name='product_catelogue'),
   path('recent_orders/',views.recent_orders,name='recent_orders'),
   path('update_stock/<int:pid>',views.update_stock,name='update_stock'),
   path('edit_profile/',views.edit_profile,name='edit_profile'),
   path('logout/',views.logout,name='logout'),
   path('sample/',views.sample,name='sample'),
   path('add_category/',views.add_category,name='add_category'),
   path('add_type/',views.add_type,name='add_type'),
   path('add_style/',views.add_style,name='add_style'),
   path('get_type/',views.get_type,name='get_type'),
   path('get_addproduct/',views.get_addproduct,name='get_addproduct')


  
  
]
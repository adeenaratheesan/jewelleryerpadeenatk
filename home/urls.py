from django.urls import path
from .import views
app_name='home'

urlpatterns=[
    path('homepage/',views.homepage,name='homepage'),
    path('login/',views.login,name='login'),
    path('alljewellery/',views.alljewellery,name='alljewellery'),
    path('earrings/',views.earrings,name='earrings'),
    path('rings/',views.rings,name='rings'),
    path('necklaces/',views.necklaces,name='necklaces'),
    path('sample/',views.sample,name='sample'),
                  
]
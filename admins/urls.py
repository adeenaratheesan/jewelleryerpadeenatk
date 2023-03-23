from django.urls import path
from .import views
app_name='admins'


urlpatterns=[
    path('index',views.index)
]
from django.urls import path
from . import views 

urlpatterns =[
    path('',views.Mainpage),
    path('Viewdetails/<id>',views.Viewdetails),
    path('showcakes/<id>',views.showcakes),
    path('login',views.login),
    path('signup',views.signup),
    path('logout',views.logout),
    path('addtocart',views.addtocart),
    path('showcart',views.showcart),
    path('modifycart',views.modifycart),
    path('makepayment',views.makepayment),
    path('search', views.search),
    ]
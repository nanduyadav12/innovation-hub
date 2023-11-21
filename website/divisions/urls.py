from django.urls import path
from . import views  # Import your views

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.blog, name='checkout'),
    path('thankyou/', views.blog, name='thankyou'),
    path('contact/', views.contact_form, name='contact_form'),
    
    
    
    
    
    
]



from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('category_homepage/<str:category>',views.category_homepage, name='category_homepage'),
    path('signup', views.signup, name='signup'),
    path('signin',views.signin, name='signin'),
    #path('homepage', views.homepage, name="homepage"),
    path('add-to-cart',views.add_to_cart,name='add_to_cart'),
    path('cart',views.cart,name='cart'),
    path('product/<int:id>', views.product, name='product'),
    path('orderitems/<int:id>', views.orderitems, name='orderitems'),
    path('orderlist', views.orderlist, name='orderlist'),
    path('cart', views.cart, name='cart'),
    path('signout', views.signout, name='signout'),
    path('delete-from-cart',views.delete_cart_item,name='delete-from-cart'),
    path('checkout',views.checkout,name='checkout'),
    path('paypal/',include('paypal.standard.ipn.urls')),
    # path('process-payment/',views.process_payment,name='process_payment'),
    path('payment-done/',views.payment_done,name='payment_done'),
    path('payment-cancelled/',views.payment_cancelled,name='payment_cancelled'),
    path('get_discounted_price', views.get_discounted_price, name='get_discounted_price'),
    path('search', views.search, name='search'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG: #add this
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
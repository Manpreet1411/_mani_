from django.conf.urls.static import static
from django.urls import path
from webproject1 import settings
from myapp import views


urlpatterns = [
    path('', views.show , name="homepage"),
    path('add-shopping-cart', views.addtoshoppingcart, name='addtoshoppingcart'),
    path('shopping-cart', views.showshoppingcart, name='shoppingcart'),
    path('shoes-product-details', views.showshoesdetails, name='productdetails'),
    path('skateboard-shoes-details/<int:pid>', views.showshoesdetails1, name='shoedetails'),
    path('shoes-categories/<int:cid>', views.productcategories, name='productcategories'),
    path('delete-product-from-cart/<int:id>', views.deleteproduct , name='deleteproduct'),
    path('sign-up', views.Signup.as_view(), name='signup'),
    path('sign-in', views.Signin, name='signin'),
    path('check-out', views.mycheckout, name='checkout'),
    path('sign-out', views.mylogout, name='logout'),
    path('order', views.finalorder, name='finalorder'),
    path('order-success', views.showordersucess, name='ordersuccess'),
    path('order-history', views.orderhistory, name='orderhistory'),
    path('order-details/<int:oid>', views.orderdetails, name='showorderdetails'),
    path('change-password', views.changepass, name='changepassword'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

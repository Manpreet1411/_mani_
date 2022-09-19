from django.conf.urls.static import static
from django.urls import path
from webproject1 import settings
from myapp import views


urlpatterns = [
    path('', views.show , name="homepage"),
    path('add-shopping-cart', views.addtoshoppingcart, name='addtoshoppingcart'),
    path('shopping-cart', views.showshoppingcart, name='shoppingcart'),
    path('shoes-product-details', views.showshoesdetails, name='productdetails'),
    path('shoes-categories/<int:cid>', views.productcategories, name='productcategories'),
    path('delete-product-from-cart/<int:id>', views.deleteproduct , name='deleteproduct'),
    path('skateboard-shoes-details/<int:pid>', views.showshoesdetails1, name='shoedetails')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    Category_name = models.CharField(max_length=120)

    def __str__(self):
        return self.Category_name

class Product(models.Model):
    # objects = models.Manager()

    Product_name = models.CharField(max_length=200)
    details=RichTextField(null=True, blank=True)
    description= RichTextField( null=True, blank=True)
    price=models.IntegerField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    product_pic=models.ImageField(upload_to='shoes_photos', blank=True , null=True)
    product_pic2 = models.ImageField(upload_to='shoes_photos', blank=True, null=True)
    product_pic3 = models.ImageField(upload_to='shoes_photos', blank=True, null=True)

    exclusive_products=models.BooleanField(null=True, default=False)
    time_of_entry=models.DateTimeField(null=True)
    values=(("1","1"),("2","2"),("3","3"),("4","4"),("5","5"),("6","6"))
    quantity=models.CharField(choices=values, max_length=1, null=True)


    def __str__(self):
        return self.Product_name

class ShoppingCart(models.Model):
    pid = models.ForeignKey(Product, on_delete=models.CASCADE)
    price=models.IntegerField()
    quantity=models.IntegerField()
    total_cost=models.IntegerField()
    sessionid=models.CharField(max_length=700, null=True)



class Order(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    address=models.TextField()
    phone=models.IntegerField()
    pincode=models.IntegerField()
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    values=(('cod','Cash on delivery'),('gpay','google pay on 123'))
    payment_mode=models.CharField(choices=values, max_length=10, null=True)

    grandtotal=models.IntegerField()
    order_date=models.DateField(auto_now_add=True)
    order_update_date=models.DateField(auto_now=True)
    values2=(('received', 'Order Received'),('process','order in process'),('shipped','order shipped'),('delivered','order delivered'),('pending','Order pending'),('cancelled','order cancelled'))
    order_status=models.CharField(choices=values2, max_length=10, null=True, default='received')



class Order_Details(models.Model):

     orderno=models.ForeignKey(Order, on_delete=models.CASCADE)
     product_id=models.ForeignKey(Product, on_delete=models.CASCADE)
     price=models.IntegerField()
     quantity=models.IntegerField()
     total_cost=models.IntegerField()







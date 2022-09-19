from ckeditor.fields import RichTextField
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





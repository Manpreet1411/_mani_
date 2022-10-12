from django.contrib import admin

# Register your models here.
from myapp.models import Category, Product, Order, Order_Details

admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Order_Details)



# admin.site.register(Product)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["Product_name", "description", "price", "product_pic","details","time_of_entry","category","exclusive_products","size"]

















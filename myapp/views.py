from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from django.urls import reverse_lazy

from myapp.models import Product, ShoppingCart, Category


def show(request):
        return render(request, "index.html")

def showshoesdetails(request):
        product_data = Product.objects.filter(exclusive_products=True)
        return render(request,"product_details.html", {'product_details_data': product_data })
        # return render(request,"product_details.html")

def showshoesdetails1(request,pid):
        shoe_details= Product.objects.get(id=pid)
        #print(shoe_details)
        return render(request, "singleproductdetails.html",  {'shoe_details_data': shoe_details })

def addtoshoppingcart(request):
    pid= int(request.POST.get('item_id'))
    price=int(float(request.POST.get("amount")))
    quantity=int(request.POST.get("quantity"))
    totalcost= price * quantity

    shoppingcartobj= ShoppingCart()
    shoppingcartobj.pid=Product(id=pid)
    shoppingcartobj.price=price
    shoppingcartobj.quantity= quantity
    shoppingcartobj.total_cost=totalcost
    if not request.session or not request.session.session_key:
        request.session.save()
    shoppingcartobj.sessionid= request.session.session_key
    shoppingcartobj.save()
    return HttpResponseRedirect(reverse_lazy('shoppingcart'))


def showshoppingcart(request):
    shoppingcartdata=ShoppingCart.objects.filter(sessionid=request.session.session_key)
    cartsum=ShoppingCart.objects.filter(sessionid=request.session.session_key).aggregate(Sum('total_cost'))
    return render(request, "shoppingcart.html", {'cartdata': shoppingcartdata, 'cartsum':cartsum})


def deleteproduct(request, id):
    cartobj=ShoppingCart.objects.get(id=id)
    cartobj.delete()
    return HttpResponseRedirect(reverse_lazy('shoppingcart'))

def productcategories(request, cid):
    product_details_data=Product.objects.filter(category=cid)
    categoryobj=Category.objects.get(id=cid)
    print(categoryobj)
    return render(request, "category_products.html",{"product_details_data":product_details_data, "categoryname":categoryobj.Category_name})




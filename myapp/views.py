from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Sum
from django.http import HttpResponseRedirect , HttpResponse , request
from django.shortcuts import render


# Create your views here.
from django.urls import reverse_lazy ,reverse
from django.views.generic import CreateView

from myapp.forms import RegisterForm , LoginForm
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
    productsdata=Product.objects.filter(category=cid)
    categoryobj=Category.objects.get(id=cid)
    print(categoryobj)
    return render(request, "category_products.html",{"productsdata":productsdata, "categoryname":categoryobj.Category_name})



class Signup(SuccessMessageMixin, CreateView):
    form_class=RegisterForm
    template_name="signup.html"
    success_url = reverse_lazy('signup')
    success_message = 'Signup Successful.You can login now'

    def dispatch(self, *args, **kwargs):
        return super(Signup,self).dispatch(*args, **kwargs)



def Signin(request):
    formobj = LoginForm(request.POST or None)
    if formobj.is_valid():
        username1= formobj.cleaned_data.get("username1")
        userobj=User.objects.get(username__iexact=username1)
        login(request,userobj)
        request.session['myusername'] = username1
        return HttpResponseRedirect(reverse('homepage'))
    else:
        return render(request, "signin.html", {"myform": formobj})











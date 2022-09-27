from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy ,reverse
from django.views.generic import CreateView
from myapp.forms import RegisterForm , LoginForm
from myapp.models import Product, ShoppingCart, Category ,Order , Order_Details



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
        request.session["sid"] = request.session.session_key
    shoppingcartobj.sessionid= request.session["sid"]
    shoppingcartobj.save()
    return HttpResponseRedirect(reverse_lazy('shoppingcart'))


def showshoppingcart(request):
    if not request.session or not request.session.session_key:
        request.session.save()
        request.session["sid"]= request.session.session_key
    shoppingcartdata=ShoppingCart.objects.filter(sessionid=request.session["sid"])
    cartsum=ShoppingCart.objects.filter(sessionid=request.session["sid"]).aggregate(Sum('total_cost'))
    request.session["cartsum"] =cartsum
    return render(request, "shoppingcart.html", {'cartdata': shoppingcartdata, 'cartsum':cartsum})


def deleteproduct(request, id):
    cartobj=ShoppingCart.objects.get(id=id)
    cartobj.delete()
    return HttpResponseRedirect(reverse_lazy('shoppingcart'))

def productcategories(request, cid):
    productsdata=Product.objects.filter(category=cid)
    categoryobj=Category.objects.get(id=cid)
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
        redirect_to=request.POST.get('next')
        username1= formobj.cleaned_data.get("username1")
        userobj=User.objects.get(username__iexact=username1)
        login(request,userobj)
        request.session['myusername'] = username1
        if redirect_to:
            return redirect(redirect_to)
        else:
          return HttpResponseRedirect(reverse('homepage'))
    else:
           return render(request, "signin.html", {"myform": formobj})

def mylogout(request):
     logout(request)
     return HttpResponseRedirect(reverse('homepage'))

@login_required()
def mycheckout(request):
    return render(request,"checkout.html")


def finalorder(request):
    username1= request.session['username']
    name= request.POST.get("name")
    address= request.POST.get("address")
    phone=request.POST.get("city")
    pincode=request.POST.get("pincode")
    city= request.POST.get("city")
    state = request.POST.get("state")
    payment_mode = request.POST.get("paymentmode")
    gtotal = request.session["cartsum"]
    grandtotal = gtotal.get("total_cost__sum")

    orderobj=Order()
    orderobj.username = User.objects.get(username=username1)
    orderobj.name=name
    orderobj.address=address
    orderobj.phone=phone
    orderobj.payment_mode=payment_mode
    orderobj.city=city
    orderobj.state=state
    orderobj.grandtotal=grandtotal
    orderobj.pincode= pincode
    orderobj.save()
    orderno = Order.objects.latest('id')

    orderdetails =Order_Details()
    shoppingcartdata= ShoppingCart.objects.filter(sessionid=request.session["sid"])
    for data in shoppingcartdata:
        orderdetails.product_id =Product(id=data.pid).id
        orderdetails.price= data.price
        orderdetails.quantity = data.quantity
        orderdetails.total_cost = data.total_cost
        orderdetails.orderno = orderno
        orderdetails.save()
    return render(request, "success.html", {"orderno": orderno})


















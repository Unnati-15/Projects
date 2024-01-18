
# Create your views here.
from collections import UserDict
from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from dog.models import Dogproduct
from cart.models import Cart,Order,OrderItem,Pay
import random
from django.contrib.auth.models import User
from signup.forms import CustomUserForm

def addtocartaction(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            dprod_id = int(request.POST.get('dproduct_id'))
            dproduct_check = Dogproduct.objects.get(id=dprod_id)
            if(dproduct_check):
                if(Cart.objects.filter(user=request.user.id,dproduct_id=dprod_id)):
                    return JsonResponse({'status':"Product already in cart"})
                else:
                    dprod_qty = int(request.POST.get('dproduct_qty'))

                    if dproduct_check.quantity >=dprod_qty:
                        Cart.objects.create(user=request.user,dproduct_id=dprod_id,dproduct_qty=dprod_qty)
                        return JsonResponse({'status':"Product added Successfully"})
                    else:
                        return JsonResponse({'status':"Only"+str(dproduct_check.quantity)+"quantity available"})
            else:
                return JsonResponse({'status':"No such dogproduct found"})

        
            
            
     
        else:
            return JsonResponse({'status':"Login to continue"})
    return redirect('/main/')

def viewcart(request):
    cart = Cart.objects.filter(user=request.user)
    context = {'cart':cart}
    return render(request,"cart.html",context)

def updatecart(request):
    if request.method=='POST':
        prod_id = int(request.POST.get('dproduct_id'))
        if(Cart.objects.filter(user=request.user,dproduct_id=prod_id)):
            prod_qty = int(request.POST.get('dproduct_qty'))
            cart = Cart.objects.get(dproduct_id=prod_id,user=request.user)
            cart.dproduct_qty = prod_qty
            cart.save()
            return JsonResponse({'status':"Updated successfully"})
    return redirect('/main/')        

def deletecartitem(request):
    if request.method=='POST':
        prod_id = int(request.POST.get('dproduct_id'))
        if(Cart.objects.filter(user=request.user,dproduct_id=prod_id)):
            cartitem = Cart.objects.get(dproduct_id=prod_id,user=request.user)
            cartitem.delete()
            return JsonResponse({'status':"Deleted successfully"})
    return redirect('/main/') 



def checkout(request):
    rawcart = Cart.objects.filter(user=request.user)
    for item in rawcart:
        if item.dproduct_qty > item.dproduct.quantity:
            Cart.objects.all().delete(dproduct_id=item.dproduct.id)

    cartitems = Cart.objects.filter(user=request.user)
    total_price = 0
    for item in cartitems:
        total_price = total_price + item.dproduct.price * item.dproduct_qty

    context = {'cartitems':cartitems,'total_price':total_price}
    return render(request,"checkout.html",context)


def placeorder(request):
    if request.method == 'POST':
        neworder = Order()
        neworder.user = request.user
        neworder.fname = request.POST.get('firstname')
        neworder.email = request.POST.get('email')
        neworder.address = request.POST.get('address')
        neworder.state = request.POST.get('state')
        neworder.city = request.POST.get('city')
        neworder.phone = request.POST.get('phone')
        neworder.zip = request.POST.get('zip')
        neworder.payment_mode = request.POST.get('payment_mode')

        cart = Cart.objects.filter(user=request.user)
        cart_total_price = 0
        for item in cart:
            cart_total_price = cart_total_price + item.dproduct.price * item.dproduct_qty

        neworder.total_price = cart_total_price
        trackno = 'superpaws'+str(random.randint(111111,999999))
        while Order.objects.filter(tracking_no=trackno) is None:
            trackno = 'superpaws'+str(random.randint(111111,999999))

        neworder.tracking_no = trackno
        neworder.save()

        neworderitems = Cart.objects.filter(user=request.user)
        for item in neworderitems:
            OrderItem.objects.create(
                order=neworder,
                product=item.dproduct,
                price=item.dproduct.price,
                quantity=item.dproduct_qty
            )

            orderproduct = Dogproduct.objects.filter(id=item.dproduct.id).first()
            orderproduct.quantity = orderproduct.quantity - item.dproduct_qty
            orderproduct.save()
        
        Cart.objects.filter(user=request.user).delete()
        
        messages.success(request,"Your order has been placed successfully")
        
    return redirect('/main/')


def myorders(request):
        orders = Order.objects.filter(user=request.user)
        context = {'orders':orders}
        return render(request,"myorders.html",context)


def orderview(request,t_no):
    order = Order.objects.filter(tracking_no=t_no).filter(user=request.user).first()
    orderitems = OrderItem.objects.filter(order=order)
    context = {'order':order,'orderitems':orderitems}
    return render(request,"view.html",context)


def payment(request):
    if request.method == 'POST':
        newpay = Pay()
        newpay.user = request.user
        newpay.nameoncard = request.POST.get('uname')
        newpay.cardno = request.POST.get('cardnumber')
        newpay.month = request.POST.get('expmonth')
        newpay.year = request.POST.get('expyear')
        newpay.cvv = request.POST.get('cvv')
        newpay.save()

        messages.success(request,"Your online payment has been successfully")
        
    return redirect('/main/')
from django.shortcuts import render,redirect
from django.contrib import messages
from dog.models import Dogproduct
from cat.models import Catproduct
from cart.models import Cart

def addtocartaction(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Dogproduct.objects.get(id=prod_id)
            if(product_check):
                if(Cart.objects.filter(user=request.user.id,product_id=prod_id)):
                    return JsonResponse({'status':"Product already in cart"})
                else:
                    prod_qty = int(request.POST.get('product_qty'))

                    if product_check.quantity >=prod_qty:
                        Cart.objects.create(user=request.user,product_id=prod_id,product_qty=prod_qty)
                        return JsonResponse({'status':"Product added Successfully"})
                    else:
                        return JsonResponse({'status':"Only"+str(product_check.quantity)+"quantity available"})
            else:
                return JsonResponse({'status':"No such product found"})
        else:
            return JsonResponse({'status':"Login to continue"})
    return redirect('/main/')




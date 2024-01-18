from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from dog.models import Dogproduct
from cat.models import Catproduct

def main(request) :
      return render(request,'index.html')
def dog(request) :
      dogpro = Dogproduct.objects.all()
      return render(request,'dog.html',{'dogpro':dogpro})
def rcpuppy(request,rcid):
     rcpuppy = Dogproduct.objects.get(id=rcid)
     data = { 'rcpuppy' : rcpuppy }
     return render(request, 'rcpuppy.html',data) 
def cat(request) :
      catpro = Catproduct.objects.all()
      return render(request,'cat.html',{'catpro':catpro})
def WK(request,wkid):
     WK = Catproduct.objects.get(id=wkid)
     data = { 'WK' : WK }
     return render(request, 'WK.html',data) 
def contactus(request) :
      return render(request,'contactus.html')
def aboutus(request) :
      return render(request,'aboutus.html')
def emergencyservices(request):
      return render(request,'emergencyservices.html')
def cart(request):
      return render(request,'cart.html')
from django.shortcuts import render
from django.http import HttpResponse
from .models import Dogproduct

# Create your views here.

def dogaction(request) :
       dogpro = Dogproduct.objects.all()
       return render(request,'dog.html',{'dogpro':dogpro})
def rcpuppy(request):
     return render(request, 'rcpuppy.html') 
def rcpuppydetails(request,rcpuppyid):
     return HttpResponse(rcpuppyid)    

     
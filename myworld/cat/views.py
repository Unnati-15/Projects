
from django.shortcuts import render
from django.http import HttpResponse
from .models import Catproduct

# Create your views here.


def cat(request) :
       catpro = Catproduct.objects.all()
       return render(request,'cat.html',{'catpro':catpro})
def WK(request):
     return render(request, 'WK.html') 
def WKdetails(request,WKid):
     return HttpResponse(WKid)      
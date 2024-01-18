from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def rcpuppy(request):
     return render(request, 'rcpuppy.html') 
def rcpuppydetails(request,rcpuppyid):
     return HttpResponse(rcpuppyid)    
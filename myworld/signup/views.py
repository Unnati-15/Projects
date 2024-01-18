from django.shortcuts import render,redirect
from django.contrib import messages
from signup.forms import CustomUserForm


# Create your views here.
def signaction(request):
      form = CustomUserForm()
      context = {'form':form}
      return render(request,'register.html',context)

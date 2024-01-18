from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from django.contrib import messages
from signup.forms import CustomUserForm


# Create your views here.
def signaction(request):
      form = CustomUserForm()
      if request.method == 'POST':
            form = CustomUserForm(request.POST)
            if form.is_valid():
                  form.save()
                  messages.success(request,"Registered Successfully : Login to continue")
                  return redirect('/login/')
      
      context = {'form':form}
      return render(request,'register.html',context)

def loginaction(request):
      if request.user.is_authenticated:
            messages.warning(request,"You are already logged in")
            return redirect('/main/')
      else:
            if request.method == 'POST':
                  name = request.POST.get('username')
                  passwd = request.POST.get('password')

                  user = authenticate(request,username=name,password=passwd)

                  
                  if user is not None:
                        login(request,user)
                        messages.success(request,"Logged In Successfully")
                        return redirect('/main/')
                        
                  
                  else:
                        messages.error(request,"Invalid Username and Password")
                        return redirect('/login/')
            return render(request,'login_page.html')

def logoutaction(request):
      if request.user.is_authenticated:
            logout(request)
            messages.success(request,"Logged out Successfully")
      return redirect('/main/')

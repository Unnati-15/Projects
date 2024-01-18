"""myworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings


from reviews.views import reviewaction
from signup.views import signaction
from signup.controller import authview
from cart.views import addtocartaction,viewcart,updatecart,deletecartitem,checkout,placeorder,myorders,orderview,payment
from login.views import loginaction
from .views import contactus
from .views import aboutus
from .views import emergencyservices
from .views import cart
from myworld import views


admin.site.site_header = "SUPERPAWS (PET SHOP) ADMINISTRATION"
admin.site.site_title = "Pet Shop Admin"

urlpatterns = [
    path('signup/',authview.signaction),
    path('login/',authview.loginaction,name='loginpage'),
    path('logout/',authview.logoutaction),
    path('main/', views.main),
    path('reviews/', reviewaction),
    path('dog/', views.dog),
    path('cat/', views.cat),
    path('rcpuppy/', views.rcpuppy),
    path('rcpuppy/<int:rcid>/', views.rcpuppy),
    path('WK/', views.WK),
    path('WK/<int:wkid>/', views.WK),
    path('contactus/', contactus),
    path('aboutus/', aboutus),
    path('emergencyservices/',emergencyservices),
    path('cart',addtocartaction),
    path('cart/',viewcart),
    path('update-cart',updatecart),
    path('delete-cart-item',deletecartitem),
    path('checkout/',checkout),
    path('payment/',payment),
    path('placeorder/',placeorder),
    path('myorders/',myorders),
    path('payment/',payment),
    path('orderview/<str:t_no>',orderview,name="orderview"),

    path('admin/', admin.site.urls),
] 

urlpatterns = urlpatterns + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)


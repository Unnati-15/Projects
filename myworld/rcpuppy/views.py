from django.shortcuts import render, HttpResponse


# Create your views here.
def rcpuppy(request):
     context = {}
     return render(request, 'rcpuppy.html', context)
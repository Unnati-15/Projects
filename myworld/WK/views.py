from django.shortcuts import render

# Create your views here.
def WK(request):
     context = {}
     return render(request, 'WK.html', context)
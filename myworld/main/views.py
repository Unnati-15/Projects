from django.shortcuts import render

# Create your views here.
def mainaction(request):
     context = {}
     return render(request, 'index.html', context)
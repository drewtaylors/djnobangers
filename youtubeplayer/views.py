from django.shortcuts import render

def index(request):    
    return render(request, 'youtubeplayer/index.html')
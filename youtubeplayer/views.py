from django.shortcuts import render

def index(request):    
    return render(request, 'youtubeplayer/index.html')

def add(request):
    return render(request, 'youtubeplayer/add.html')

def queue(request):
    return render(request, 'youtubeplayer/queue.html')
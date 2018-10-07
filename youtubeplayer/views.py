from django.shortcuts import render
from .forms import YTVideoForm
from .models import YTVideo

def index(request):
    if request.method == 'POST':
        yt = YTVideoForm(request.POST)
        if yt.is_valid():
            data = yt.save()
            return render(request, 'youtubeplayer/index.html', {
                'youtube_id': data.url,
                'next_youtube_id': "iVbqc_a3hYo",
                'yt': yt
            })
    else:
        yt = YTVideoForm()

    return render(request, 'youtubeplayer/index.html', {
        'youtube_id': 'cUTCIO_zLyU',
        'yt': yt
    })

def add(request):
    return render(request, 'youtubeplayer/add.html')

def queue(request):
    return render(request, 'youtubeplayer/queue.html')
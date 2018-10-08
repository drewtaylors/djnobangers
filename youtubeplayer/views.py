from django.shortcuts import render
from .forms import YTVideoForm
from .models import YTVideo
from django.http import HttpResponse

def index(request):
    # if request.method == 'POST':
    #     yt = YTVideoForm(request.POST)
    #     if yt.is_valid():
    #         data = yt.save()
    #         return render(request, 'index.html', {
    #             'youtube_id': data.url,
    #             'next_youtube_id': "iVbqc_a3hYo",
    #             'yt': yt
    #         })
    #     return HttpResponse(request.POST['item_text'])
    # else:
    #     yt = YTVideoForm()

    yt = YTVideoForm()

    return render(request, 'index.html', {
        'youtube_id': 'cUTCIO_zLyU',
        'yt': yt,
        'new_item_text': request.POST.get('item_text', ''),
    })

def add(request):
    return render(request, 'add.html')

def queue(request):
    return render(request, 'queue.html')
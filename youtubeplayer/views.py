from django.shortcuts import redirect, render
from .forms import YTVideoForm
from .models import YTVideo
from .models import Item
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

    # yt = YTVideoForm()
    # item = Item()
    # item.text = request.POST.get('item_text', '')
    # item.save()

    # return render(request, 'index.html', {
    #     'youtube_id': 'cUTCIO_zLyU',
    #     'yt': yt,
    #     'new_item_text': item.text,
    # })
    
    items = Item.objects.all()
    return render(request, 'index.html')

def new_list(request):
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/youtubeplayer/the-only-list-in-the-world/')

def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

def add(request):
    return render(request, 'add.html')

def queue(request):
    return render(request, 'queue.html')
    
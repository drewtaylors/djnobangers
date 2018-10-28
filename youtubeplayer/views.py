from django.shortcuts import redirect, render
from .forms import YTVideoForm
from .models import YTVideo
from .models import Item, List
from django.http import HttpResponse
from .utils import parse_youtube_url

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
    list_ = List.objects.create()
    Item.objects.create(url=parse_youtube_url(request.POST['item_url']), list=list_)
    return redirect(f'/youtubeplayer/{list_.id}/')

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_, 'next_youtube_url': list_.item_set.first().url})

def add_url(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(url=parse_youtube_url(request.POST['item_url']), title='', list=list_)
    return redirect(f'/youtubeplayer/{list_.id}/')

def add(request):
    return render(request, 'add.html')

def queue(request):
    return render(request, 'queue.html')
    
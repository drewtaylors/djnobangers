from django.shortcuts import redirect, render
from .forms import YTVideoForm
from .models import YTVideo
from .models import Item, List
from django.http import HttpResponse
from .utils import parse_youtube_url
from youtubeplayer.youtube import YouTubeClient

def index(request):
    items = Item.objects.all()
    return render(request, 'youtubeplayer/index.html')

def new_list(request):
    list_ = List.objects.create()
    url = parse_youtube_url(request.POST['item_url'])
    title = YouTubeClient.get_youtube_title(url)
    Item.objects.create(url=url, title=title, media='youtube', list=list_)
    return redirect(f'/youtubeplayer/{list_.id}/')

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'youtubeplayer/list.html', {'list': list_, 'list_id': list_id})

def add_url(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(url=parse_youtube_url(request.POST['item_url']), title='', media='', list=list_)
    return redirect(f'/youtubeplayer/{list_.id}/')
    
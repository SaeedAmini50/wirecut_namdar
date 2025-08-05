from django.shortcuts import render
from django.http import HttpResponse
from textInfo.models import TextEntry, Number, MainPageImage, Video

def home(request):
    main_images = MainPageImage.objects.filter(is_active=True).order_by('display_order')
    videos = Video.objects.filter(is_active=True)
    return render(request, 'index.html', {
        'main_images': main_images,
        'videos': videos
    })


def footer (requset):
    return render(requset , 'footer.html')



def header (requset):
    return render(requset , 'header.html')


def about (requset):
    return render(requset , 'about.html')

def blog (requset):
    return render(requset , 'blog.html')


def service (requset):
    return render(requset , 'service.html')

def team (requset):
    return render(requset , 'team.html')

def contact (requset):
    return render(requset , 'contact.html')

def number2(request):
    numbers = Number.objects.all()[:4]
    return render(request, 'number2.html', {'numbers': numbers})

def home_view(request):
    return render(request, 'single.html')

def text_list_view(request):
    texts = TextEntry.objects.filter(is_visible=True).order_by('unique_id')
    return render(request, 'text_list.html', {'texts': texts})

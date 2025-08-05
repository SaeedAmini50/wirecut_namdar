from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from .models import TextEntry, Number, Project,Video

# Create your views here.

class PublicTextListView(ListView):
    model = TextEntry
    template_name = 'textInfo/text_list.html'
    context_object_name = 'texts'

    def get_queryset(self):
        return TextEntry.objects.filter(is_visible=True).order_by('unique_id')

@method_decorator(staff_member_required, name='dispatch')
class AdminTextListView(ListView):
    model = TextEntry
    template_name = 'textInfo/admin_text_list.html'
    context_object_name = 'texts'

    def get_queryset(self):
        return TextEntry.objects.all().order_by('unique_id')
    
def cnc(request):
    texts = TextEntry.objects.filter(is_visible=True, category__name='cnc').order_by('unique_id')
    numbers = Number.objects.all()
    return render(request, 'cnc.html', {'texts': texts, 'numbers': numbers})



def wirecut(request):
    texts = TextEntry.objects.filter(is_visible=True, category__name='wirecut').order_by('unique_id')
    numbers = Number.objects.all()
    return render(request, 'wirecut.html', {'texts': texts, 'numbers': numbers})


def portfolio(request):
    active_projects = Project.objects.filter(is_active=True).order_by('display_order')
    return render(request, 'portfolio.html', {'active_projects': active_projects})



def video_view(request):
    videos = Video.objects.filter(is_active=True)
    return render(request, 'main/index.html', {'videos': videos})

from django.urls import path
from . import views

app_name = 'textInfo'

urlpatterns = [
    path('texts/', views.PublicTextListView.as_view(), name='text_list'),
    path('admin/texts/', views.AdminTextListView.as_view(), name='admin_text_list'),
    path('cnc/', views.cnc, name='cnc'),
    path('wirecut/', views.wirecut, name='wirecut'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('videos/', views.video_view, name='videos'),
] 
 
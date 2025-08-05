from django.urls import path
from project.views import home,about,blog,service,team,contact,header,footer,number2


app_name = 'project'
urlpatterns = [
    
    path('', home , name='home'),
    path('about/', about , name='about'),
    path('blog/', blog , name='blog'),
    path('service/', service , name='service'),
    path('team/', team , name='team'),
    path('contact/', contact , name='contact'),
    path('header/', header , name='header'),
    path('footer/', footer , name='footer'),
    path('number2/', number2 , name='number2'),
    

    
]
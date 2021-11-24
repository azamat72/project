from django.urls import path
from . views import *

app_name = "leads"

urlpatterns = [
    path('', index, name = 'index'),
    path('about/', about, name = 'about'),
    path('news/', news, name = 'news'),
    path('contacts/', contacts, name = 'contacts'),
    path('leads/<pk>/', leads_abc),
    path('create/', create, name='create')
    
    
]
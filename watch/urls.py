from django.urls import path
from . import views


#create Urls
urlpatterns =[
    path('', views.index, name= 'index'),
    
]
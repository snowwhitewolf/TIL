from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('catch/', views.catch,name='catch'),
    path('throw/', views.throw,name='throw'),
    path('greeting/', views.greeting,name='greeting'),
]

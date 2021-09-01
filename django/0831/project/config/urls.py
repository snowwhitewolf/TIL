"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from articles import views as art_views
# from accounts import views as acc_views

urlpatterns = [
    #path('accounts/index/', acc_views.index),
    path('accounts/', include('accounts.urls')),
    path('articles/', include('articles.urls')),
    # path('dinner/<str:menu>/<int:person>/',art_views.dinner),
    # path('hello/<str:name>/', art_views.hello),
    # path('dinner/<menu>/<int:person>/', art_views.read),
    # path('catch/', art_views.catch),
    # path('throw/', art_views.throw),
    # path('greeting/', art_views.greeting),
    # path('articles/index/', art_views.index),
    path('admin/', admin.site.urls),
]

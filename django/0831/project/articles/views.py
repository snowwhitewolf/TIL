from django.shortcuts import render

def index(request):
    title = 'title'
    return render(request, 'articles/index.html',{'name' : 'JH'})

def greeting(request):
    foods = ['Apple', 'Banana', 'Peach']
    info = {
        'name': 'JH'
    }

    context = {
        'foods' : foods,
        'info' : info
    }
    return render(request,'articles/greeting.html', context)

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    title = request.GET.get('articles/title')
    context = {
        'title' : title
    }
    return render(request, 'articles/catch.html', context)

def read(request, menu, person):
    context = {
        {'menu' : menu},
        {'person' : person}
    }
    return render(request, 'articles/read.html',context)
def hello(request, name):
    return render(request, 'articles/hello.html', {'name': name})
def dinner(request, menu,person):
    context = {
        'menu' : menu,
        'person' : person
    }
    return render(request, 'articles/dinner.html', context)
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST,require_http_methods,require_safe

def signup(request):
    if request.user.is_authenticated:
        return redirect('community:index')
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            auth_login(request,user)
            return redirect('community:index')
    else:
        form = UserCreationForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/signup.html',context)

def login(request):
    if request.user.is_authenticated:
        return redirect('community:index')
    if request.method=="POST":
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            auth_login(request,form.get_user())
            return redirect('community:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/login.html',context)

def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('community:index')
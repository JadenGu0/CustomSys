from django.http import  HttpResponse,HttpResponseRedirect
from django.shortcuts import render,render_to_response,redirect
from django.contrib.auth import authenticate, login

def show_login(request):
    return render_to_response('login.html')

def my_login(request):
    if request.method=='POST':
        name=request.POST['name']
        password=request.POST['password']
        user = authenticate(username=name,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect("/custom")


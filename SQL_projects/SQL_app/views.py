from django.shortcuts import render, HttpResponse, redirect
from SQL_app.models import *

def index(request,):
    context = {
        'users' : Users.objects.all()
    }
    return render(request,"index.html",context)

def insert(request):
    if request.method == 'POST':
        Users.objects.create (first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],age=request.POST['age'])
    return redirect('/')
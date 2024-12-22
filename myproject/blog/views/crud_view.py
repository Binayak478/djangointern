from django.shortcuts import render

def create(request):
    return render(request,'main/create.html')

def edit(request):
    return render(request,'main/edit.html')

def home(request):
    return render(request,'main/home.html')

def single_blog(request):
    return render(request,'main/single_blog.html')
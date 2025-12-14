from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'blog_system/blog/home.html')

def about(request):
    return render(request, 'blog_system/blog/about.html')

def detail(request, sla, algo):
    return HttpResponse(f"Hello, world. You're at the blog index. {sla}")